import logging

from colorama import Fore, Style, init

from src.library import Library, LibraryManager
from src.logger import configure_logging

init(autoreset=True)

logger = logging.getLogger(__name__)


def main() -> None:
    configure_logging()
    logger.info("Starting the library management program.")

    library = Library()
    manager = LibraryManager(library)

    try:
        while True:
            try:
                command = (
                    input(
                        f"{Fore.YELLOW}Enter command (add, remove, show, exit): "
                        f"{Style.RESET_ALL}"
                    )
                    .strip()
                    .lower()
                )

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
                                "Unexpected end of input when adding a book."
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
                                "Unexpected end of input when removing a book."
                            )
                    case "show":
                        manager.show_books()
                    case "exit":
                        logger.info("End of work by command exit.")
                        break
                    case "":
                        logger.warning("Empty command.")
                        logger.info("Enter command: add, remove, show or exit.")
                    case _:
                        logger.info("Invalid command. Please try again.")
            except EOFError:
                logger.info("End of work: end of input (EOF).")
                break
    except KeyboardInterrupt:
        logger.info("End of work: interrupted by user.")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.getLogger(__name__).exception("Critical error")
        raise
