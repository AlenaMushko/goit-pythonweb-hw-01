from colorama import Fore, Style

from src.library.book import Book
from src.library.interfaces import LibraryInterface
from src.logger import Logger


class Library(LibraryInterface):
    def __init__(self) -> None:
        self._books: list[Book] = []
        self._log = Logger()

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
        self._log.info(
            f"Додано книгу: {title.strip()} ({author.strip()}, {year.strip()})"
        )

    def remove_book(self, title: str) -> bool:
        if not title.strip():
            self._log.warning("Спроба видалити книгу з порожньою назвою.")
            return False
        for book in self._books:
            if book.title == title.strip():
                self._books.remove(book)
                self._log.info(f"Видалено книгу: {book.title}")
                return True
        self._log.warning(f"Книгу не знайдено для видалення: {title.strip()}")
        return False

    def show_books(self) -> None:
        if not self._books:
            self._log.info("Список книг порожній.")
            print(f"{Fore.YELLOW}У бібліотеці ще немає книг.{Style.RESET_ALL}")
            return
        self._log.info(f"Показано список книг ({len(self._books)} шт.).")
        for book in self._books:
            print(
                f"{Fore.CYAN}Title: {book.title}, "
                f"Author: {book.author}, Year: {book.year}{Style.RESET_ALL}"
            )
