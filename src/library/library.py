import logging

from src.library.book import Book
from src.library.interfaces import LibraryInterface

logger = logging.getLogger(__name__)


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: list[Book] = []

    def _validate_book_fields(self, title: str, author: str, year: str) -> None:
        if not title.strip():
            raise ValueError("Title is required.")
        if not author.strip():
            raise ValueError("Author is required.")
        if not year.strip():
            raise ValueError("Year is required.")
        try:
            y = int(year.strip())
        except ValueError as e:
            raise ValueError("Year must be an integer.") from e
        if y < 0 or y > 9999:
            raise ValueError("Year must be between 0 and 9999.")

    def add_book(self, title: str, author: str, year: str) -> None:
        self._validate_book_fields(title, author, year)
        self._books.append(Book(title.strip(), author.strip(), year.strip()))
        logger.info(
            "Added book: %s (%s, %s)",
            title.strip(),
            author.strip(),
            year.strip(),
        )

    def remove_book(self, title: str) -> bool:
        if not title.strip():
            logger.warning("Attempt to delete a book with an empty title.")
            return False
        for book in self._books:
            if book.title == title.strip():
                self._books.remove(book)
                logger.info("Deleted book: %s", book.title)
                return True
        logger.warning("Book not found for deletion: %s", title.strip())
        return False

    def show_books(self) -> None:
        if not self._books:
            logger.info("The list of books is empty. The library has no books yet.")
            return
        logger.info("Shown list of books (%d items).", len(self._books))
        for book in self._books:
            logger.info(
                "Title: %s, Author: %s, Year: %s",
                book.title,
                book.author,
                book.year,
            )
