import logging

from colorama import Fore, Style, init

from src.library import Library, LibraryManager
from src.logger import configure_logging

init(autoreset=True)

logger = logging.getLogger(__name__)


def main() -> None:
    configure_logging()
    logger.info("Запуск програми керування бібліотекою.")

    library = Library()
    manager = LibraryManager(library)

    try:
        while True:
            try:
                command = input(
                    f"{Fore.YELLOW}Enter command (add, remove, show, exit): "
                    f"{Style.RESET_ALL}"
                ).strip().lower()

                match command:
                    case "add":
                        try:
                            title = input(
                                f"{Fore.YELLOW}Enter book title: {Style.RESET_ALL}"
                            ).strip()
                            author = input(
                                f"{Fore.YELLOW}Enter book author: {Style.RESET_ALL}"
                            ).strip()
                            year = input(
                                f"{Fore.YELLOW}Enter book year: {Style.RESET_ALL}"
                            ).strip()
                            manager.add_book(title, author, year)
                        except EOFError:
                            logger.warning(
                                "Несподіваний кінець вводу під час додавання книги."
                            )
                    case "remove":
                        try:
                            title = input(
                                f"{Fore.YELLOW}Enter book title to remove: "
                                f"{Style.RESET_ALL}"
                            ).strip()
                            manager.remove_book(title)
                        except EOFError:
                            logger.warning(
                                "Несподіваний кінець вводу під час видалення."
                            )
                    case "show":
                        manager.show_books()
                    case "exit":
                        logger.info("Завершення роботи за командою exit.")
                        break
                    case "":
                        logger.warning("Порожня команда.")
                        logger.info(
                            "Введіть команду: add, remove, show або exit."
                        )
                    case _:
                        logger.info("Invalid command. Please try again.")
            except EOFError:
                logger.info("Завершення: кінець вводу (EOF).")
                break
    except KeyboardInterrupt:
        logger.info("Завершення: перервано користувачем.")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.getLogger(__name__).exception("Критична помилка")
        raise
