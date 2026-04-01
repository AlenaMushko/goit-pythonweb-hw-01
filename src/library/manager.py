from colorama import Fore, Style

from src.library.interfaces import LibraryInterface
from src.logger import Logger


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self._library = library
        self._log = Logger()

    def add_book(self, title: str, author: str, year: str) -> None:
        try:
            self._library.add_book(title, author, year)
            print(
                f"{Fore.GREEN}Книгу успішно додано.{Style.RESET_ALL}"
            )
        except ValueError as e:
            self._log.error(f"Помилка додавання книги: {e}")
            print(f"{Fore.RED}{e}{Style.RESET_ALL}")
        except Exception as e:
            self._log.error(f"Неочікувана помилка при додаванні: {e}")
            print(
                f"{Fore.RED}Сталася помилка. Спробуйте ще раз.{Style.RESET_ALL}"
            )

    def remove_book(self, title: str) -> None:
        try:
            removed = self._library.remove_book(title)
            if removed:
                print(
                    f"{Fore.GREEN}Книгу успішно видалено.{Style.RESET_ALL}"
                )
            else:
                print(
                    f"{Fore.YELLOW}Книгу з такою назвою не знайдено.{Style.RESET_ALL}"
                )
        except Exception as e:
            self._log.error(f"Неочікувана помилка при видаленні: {e}")
            print(
                f"{Fore.RED}Сталася помилка при видаленні.{Style.RESET_ALL}"
            )

    def show_books(self) -> None:
        try:
            self._library.show_books()
        except Exception as e:
            self._log.error(f"Неочікувана помилка при показі книг: {e}")
            print(
                f"{Fore.RED}Не вдалося показати список книг.{Style.RESET_ALL}"
            )
