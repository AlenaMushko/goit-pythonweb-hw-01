from colorama import Fore, Style

from src.vehicles.base import Vehicle


class Car(Vehicle):
    def __init__(self, make: str, model: str, region_spec: str) -> None:
        self.make = make
        self.model = model
        self.region_spec = region_spec

    def start_engine(self) -> None:
        msg = (
            f"{Fore.YELLOW}{self.make} {self.model} ({self.region_spec}): "
            f"Двигун запущено{Style.RESET_ALL}"
        )
        print(msg)
