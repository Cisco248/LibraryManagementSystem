from abc import ABC, abstractmethod


class API(ABC):

    def __init__(self, isbn: str):
        self.isbn = isbn

    @abstractmethod
    def get_book_info(self) -> dict:
        pass


class Repository(ABC):

    @abstractmethod
    def get_one(self, isbn: str) -> str:
        pass

    @abstractmethod
    def get_all(self) -> str:
        pass

    @abstractmethod
    def add(self, data: object) -> str:
        pass

    @abstractmethod
    def update(self, isbn: str, updates: dict) -> str:
        pass

    @abstractmethod
    def delete(self, isbn: str) -> str:
        pass

    @abstractmethod
    def search(self, **data) -> str:
        pass
