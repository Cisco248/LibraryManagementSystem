import csv


class BookService:
    def __init__(self, file_path: str, header: list[str]) -> None:
        self.file_path = file_path
        self.header = header
        pass

    def read_all(self) -> list[dict]:
        with open(self.file_path, "r", newline="") as f:
            return list(csv.DictReader(f))

    def write_all(self, data: list[dict]):
        with open(self.file_path, "w", newline="") as f:
            writter = csv.DictWriter(f, fieldnames=self.header)
            writter.writeheader()
            writter.writerows(data)
