import copy
import logging

from colorama import Fore, Style, init

init(autoreset=True)

_LEVEL_COLORS = {
    logging.DEBUG: Fore.CYAN,
    logging.INFO: Fore.GREEN,
    logging.WARNING: Fore.YELLOW,
    logging.ERROR: Fore.RED,
    logging.CRITICAL: Fore.RED + Style.BRIGHT,
}


class ColoredFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        r = copy.copy(record)
        color = _LEVEL_COLORS.get(record.levelno, "")
        r.levelname = f"{color}{record.levelname}{Style.RESET_ALL}"
        return super().format(r)


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            log = logging.getLogger(__name__)
            log.setLevel(logging.INFO)
            handler = logging.StreamHandler()
            handler.setFormatter(
                ColoredFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            )
            log.addHandler(handler)
            cls._instance._log = log
        return cls._instance

    def debug(self, message: str) -> None:
        self._log.debug(message)

    def info(self, message: str) -> None:
        self._log.info(message)

    def warning(self, message: str) -> None:
        self._log.warning(message)

    def error(self, message: str) -> None:
        self._log.error(message)
