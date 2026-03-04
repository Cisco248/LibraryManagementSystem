import cv2
import zxingcpp
import numpy as np
import csv
import os
import threading
import time
from datetime import datetime
from repository import BookAPIFactory


class BarCodeScanner:

    def __init__(self, out_path: str, column_titles: list) -> None:

        self.out_path = out_path
        self.column_titles = column_titles
        self.scanned = set()
        self.last_scan_time = 0

        self.path_checker()

        self.hints = zxingcpp.BarcodeFormats(
            [zxingcpp.BarcodeFormat.EAN13, zxingcpp.BarcodeFormat.EAN8]
        )

        self.sharpen_kernel = np.array(
            [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]], dtype=np.float32
        )

    def path_checker(self) -> None:
        """
        # Path Checker

        Create CSV file if not exists

        ## Params:
            #### self.column_titles
                [ "ISBN", "Title", "Author", "Publisher", "Published", "Scanned At" ]
        """
        if not os.path.exists(self.out_path):
            with open(self.out_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(self.column_titles)

    def save_to_csv(self, info: dict):
        """Save to CSV"""
        with open(self.out_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                [
                    info["isbn"],
                    info["title"],
                    info["author"],
                    info["publisher"],
                    info["publication_year"],
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                ]
            )

    def get_book_info(self, isbn: str):

        try:
            return BookAPIFactory.get_book_info(isbn)
        except Exception as e:
            print(f"Error fetching ISBN {isbn}: {e}")
            return None

    def process_isbn(self, isbn: str):
        """Process ISBN (threaded)"""

        if len(isbn) not in [10, 13]:
            return

        if len(isbn) == 13 and not isbn.startswith(("978", "979")):
            print(f"Not a book ISBN: {isbn} — skipping")
            return

        print(f"\nISBN detected: {isbn}")
        print("Looking up book details...")

        info = self.get_book_info(isbn)

        if info:
            print(f"Title     : {info['title']}")
            print(f"Author    : {info['author']}")
            print(f"Publisher : {info['publisher']}")
            print(f"Published : {info['publication_year']}")

            self.save_to_csv(info)
            print(f"Saved to {self.out_path}")
        else:
            print(f"No book found for ISBN: {isbn}")

    def try_scan(self, gray):
        """Barcode detection helper"""

        results = zxingcpp.read_barcodes(gray, formats=self.hints)

        if results:
            return results

        sharpened = cv2.filter2D(gray, -1, self.sharpen_kernel)

        results = zxingcpp.read_barcodes(sharpened, formats=self.hints)

        if results:
            return results

        scaled = cv2.resize(gray, None, fx=1.5, fy=1.5)

        results = zxingcpp.read_barcodes(scaled, formats=self.hints)

        if results:
            return results

        return zxingcpp.read_barcodes(
            cv2.filter2D(scaled, -1, self.sharpen_kernel), formats=self.hints
        )

    def start_scanner(self):

        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
        cap.set(cv2.CAP_PROP_FPS, 30)

        print("Point camera at a book barcode. Press 'q' to quit.")

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
            results = self.try_scan(gray)

            if results:
                for result in results:
                    isbn = result.text
                    current_time = time.time()
                    # only scan if 3 seconds have passed since last scan
                    if isbn not in self.scanned and (current_time - last_scan_time) > 3:
                        self.scanned.add(isbn)
                        last_scan_time = current_time
                        thread = threading.Thread(
                            target=self.process_isbn, args=(isbn,)
                        )
                        thread.daemon = True
                        thread.start()

                    cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), 4)
                    cv2.putText(
                        frame,
                        f"FOUND: {isbn}",
                        (center_x - 160, center_y + radius + 30),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2,
                    )
            else:
                cv2.circle(frame, (center_x, center_y), radius, (255, 255, 0), 2)
                cv2.putText(
                    frame,
                    "Point barcode inside circle",
                    (center_x - 160, center_y + radius + 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2,
                )

            cv2.imshow("ISBN Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()
        print(f"\nAll done! Results saved to {self.out_path}")
