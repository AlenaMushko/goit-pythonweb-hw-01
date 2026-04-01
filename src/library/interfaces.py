from abc import ABC, abstractmethod


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: str) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass
