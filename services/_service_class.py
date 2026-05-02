from abc import ABC, abstractmethod


class Controller(ABC):

    @abstractmethod
    def handle_get_one(self, isbn: str):
        pass

    @abstractmethod
    def handle_get_all(self):
        pass

    @abstractmethod
    def handle_add(self, data: dict):
        pass

    @abstractmethod
    def handle_update(self, isbn: str, data: dict):
        pass

    @abstractmethod
    def handle_delete(self, isbn: str):
        pass
