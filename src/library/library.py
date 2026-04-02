import logging

from src.library.book import Book
from src.library.interfaces import LibraryInterface

logger = logging.getLogger(__name__)


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: list[Book] = []

    def _validate_book_fields(self, title: str, author: str, year: str) -> None:
        if not title.strip():
            raise ValueError("Назва книги не може бути порожньою.")
        if not author.strip():
            raise ValueError("Автор не може бути порожнім.")
        if not year.strip():
            raise ValueError("Рік видання не може бути порожнім.")
        try:
            y = int(year.strip())
        except ValueError as e:
            raise ValueError("Рік має бути цілим числом.") from e
        if y < 0 or y > 9999:
            raise ValueError("Рік має бути в діапазоні 0–9999.")

    def add_book(self, title: str, author: str, year: str) -> None:
        self._validate_book_fields(title, author, year)
        self._books.append(Book(title.strip(), author.strip(), year.strip()))
        logger.info(
            "Додано книгу: %s (%s, %s)",
            title.strip(),
            author.strip(),
            year.strip(),
        )

    def remove_book(self, title: str) -> bool:
        if not title.strip():
            logger.warning("Спроба видалити книгу з порожньою назвою.")
            return False
        for book in self._books:
            if book.title == title.strip():
                self._books.remove(book)
                logger.info("Видалено книгу: %s", book.title)
                return True
        logger.warning("Книгу не знайдено для видалення: %s", title.strip())
        return False

    def show_books(self) -> None:
        if not self._books:
            logger.info("Список книг порожній. У бібліотеці ще немає книг.")
            return
        logger.info("Показано список книг (%d шт.).", len(self._books))
        for book in self._books:
            logger.info(
                "Title: %s, Author: %s, Year: %s",
                book.title,
                book.author,
                book.year,
            )
