import cv2
import zxingcpp
import numpy as np
import requests
import csv
import os
import threading
import time
from datetime import datetime

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
cap.set(cv2.CAP_PROP_FPS, 30)

print("Point camera at a book barcode. Press 'q' to quit.")

scanned = set()
csv_file = "scanned_books.csv"

hints = zxingcpp.BarcodeFormats([
    zxingcpp.BarcodeFormat.EAN13,
    zxingcpp.BarcodeFormat.EAN8
])

sharpen_kernel = np.array([[-1,-1,-1],
                            [-1, 9,-1],
                            [-1,-1,-1]], dtype=np.float32)

if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ISBN", "Title", "Author", "Publisher", "Published", "Scanned At"])

def get_book_info(isbn):
    try:
        # try Google Books first
        url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data["totalItems"] > 0:
            book = data["items"][0]["volumeInfo"]
            return {
                "isbn": isbn,
                "title": book.get("title", "Unknown"),
                "author": ", ".join(book.get("authors", ["Unknown"])),
                "publisher": book.get("publisher", "Unknown"),
                "publication_year": int(book.get("publishedDate", "2000")[:4]),
                "book_type": "printed",
                "status": "available",
                "file_format": "",
                "file_size": 0.0,
            }

        # fallback to Open Library
        print("  Not found on Google Books, trying Open Library...")
        ol_url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
        ol_response = requests.get(ol_url, timeout=5)
        ol_data = ol_response.json()

        key = f"ISBN:{isbn}"
        if key in ol_data:
            book = ol_data[key]
            authors = ", ".join([a["name"] for a in book.get("authors", [])]) or "Unknown"
            pub_date = book.get("publish_date", "2000")
            year = int(''.join(filter(str.isdigit, pub_date))[:4]) if pub_date else 2000
            return {
                "isbn": isbn,
                "title": book.get("title", "Unknown"),
                "author": authors,
                "publisher": ", ".join([p["name"] for p in book.get("publishers", [])]) or "Unknown",
                "publication_year": year,
                "book_type": "printed",
                "status": "available",
                "file_format": "",
                "file_size": 0.0,
            }

        return None

    except Exception as e:
        print(f"Error looking up ISBN {isbn}: {e}")
        return None

def process_isbn(isbn):
    if len(isbn) not in [10, 13]:
        return
    if len(isbn) == 13 and not isbn.startswith(("978", "979")):
        print(f"Not a book ISBN: {isbn} — skipping")
        return

    print(f"\nISBN detected: {isbn}")
    print("Looking up book details...")
    info = get_book_info(isbn)

    if info:
        print(f"  Title     : {info['title']}")
        print(f"  Author    : {info['author']}")
        print(f"  Publisher : {info['publisher']}")
        print(f"  Published : {info['publication_year']}")

        #apita meeka database ekta return karanna oone dictionary output ekk
        with open(csv_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                info["isbn"],
                info["title"],
                info["author"],
                info["publisher"],
                info["publication_year"],
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])
        print(f"  Saved to {csv_file}")
    # return   
    else:
        print(f"  No book found for ISBN: '{isbn}'")

def try_scan(gray):
    results = zxingcpp.read_barcodes(gray, formats=hints)
    if results:
        return results
    sharpened = cv2.filter2D(gray, -1, sharpen_kernel)
    results = zxingcpp.read_barcodes(sharpened, formats=hints)
    if results:
        return results
    scaled = cv2.resize(gray, None, fx=1.5, fy=1.5)
    results = zxingcpp.read_barcodes(scaled, formats=hints)
    if results:
        return results
    return zxingcpp.read_barcodes(cv2.filter2D(scaled, -1, sharpen_kernel), formats=hints)

last_scan_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]
    center_x, center_y = width // 2, height // 2
    radius = 200

    x1 = max(center_x - radius, 0)
    y1 = max(center_y - radius, 0)
    x2 = min(center_x + radius, width)
    y2 = min(center_y + radius, height)
    cropped = frame[y1:y2, x1:x2]

    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    gray = cv2.convertScaleAbs(gray, alpha=1.3, beta=10)
    results = try_scan(gray)

    if results:
        for result in results:
            isbn = result.text
            current_time = time.time()
            # only scan if 3 seconds have passed since last scan
            if isbn not in scanned and (current_time - last_scan_time) > 3:
                scanned.add(isbn)
                last_scan_time = current_time
                thread = threading.Thread(target=process_isbn, args=(isbn,))
                thread.daemon = True
                thread.start()

            cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 4)
            cv2.putText(frame, f"FOUND: {isbn}", (center_x - 160, center_y + radius + 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    else:
        cv2.circle(frame, (center_x, center_y), radius, (255, 255, 0), 2)
        cv2.putText(frame, "Point barcode inside circle", (center_x - 160, center_y + radius + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("ISBN Scanner", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print(f"\nAll done! Results saved to {csv_file}")