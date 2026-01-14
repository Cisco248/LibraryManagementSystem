from dataclasses import asdict, dataclass


@dataclass
class BookModel:
    """
    A class representing a Book in a library system.

    Attributes:
        isbn (int): The unique ISBN number of the book.
        title (str): The title of the book.
        author (str): The author of the book.
        publisher (str): The publisher of the book.
        status (bool): Availability status of the book. True if available, False if unavailable.

    Methods:
        to_dict() -> dict:
            Converts the BookModel instance into a dictionary.
        __post_init__():
            Validate data after initialization.
    """

    isbn: int
    title: str
    author: str
    publisher: str
    status: bool

    def to_dict(self) -> dict:
        return asdict(self)

    def __post_init__(self):
        if not self.isbn:
            raise ValueError("ISBN Cannot be empty!")
        if not self.title:
            raise ValueError("Tiitle Cannot be empty")
