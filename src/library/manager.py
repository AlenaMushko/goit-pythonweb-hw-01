import logging

from src.library.interfaces import LibraryInterface

logger = logging.getLogger(__name__)


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self._library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        try:
            self._library.add_book(title, author, year)
        except ValueError as e:
            logger.error("Операція додавання не виконана: %s", e)

    def remove_book(self, title: str) -> bool:
        try:
            return self._library.remove_book(title)
        except Exception:
            logger.exception("Неочікувана помилка при видаленні книги")
            return False

    def show_books(self) -> None:
        try:
            self._library.show_books()
        except Exception:
            logger.exception("Неочікувана помилка при відображенні книг")
