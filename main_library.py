from colorama import Fore, Style, init

from src.library import Library, LibraryManager
from src.logger import Logger

init(autoreset=True)


def main() -> None:
    log = Logger()
    log.info("Запуск програми керування бібліотекою.")

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
                            log.warning("Несподіваний кінець вводу під час add.")
                            print(
                                f"{Fore.RED}Ввід перервано.{Style.RESET_ALL}"
                            )
                    case "remove":
                        try:
                            title = input(
                                f"{Fore.YELLOW}Enter book title to remove: "
                                f"{Style.RESET_ALL}"
                            ).strip()
                            manager.remove_book(title)
                        except EOFError:
                            log.warning("Несподіваний кінець вводу під час remove.")
                            print(
                                f"{Fore.RED}Ввід перервано.{Style.RESET_ALL}"
                            )
                    case "show":
                        manager.show_books()
                    case "exit":
                        log.info("Завершення роботи за командою exit.")
                        print(f"{Fore.CYAN}До побачення!{Style.RESET_ALL}")
                        break
                    case "":
                        log.warning("Порожня команда.")
                        print(
                            f"{Fore.YELLOW}Введіть команду: add, remove, show або exit."
                            f"{Style.RESET_ALL}"
                        )
                    case _:
                        log.warning(f"Невідома команда: {command!r}.")
                        print(
                            f"{Fore.RED}Invalid command. Please try again."
                            f"{Style.RESET_ALL}"
                        )
            except EOFError:
                log.info("Завершення: кінець вводу (EOF).")
                print(f"{Fore.CYAN}До побачення!{Style.RESET_ALL}")
                break
    except KeyboardInterrupt:
        log.info("Завершення: перервано користувачем (Ctrl+C).")
        print(
            f"\n{Fore.YELLOW}Роботу перервано. До побачення!{Style.RESET_ALL}"
        )


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        Logger().error(f"Критична помилка: {e}")
        print(f"{Fore.RED}Критична помилка програми.{Style.RESET_ALL}")
        raise
