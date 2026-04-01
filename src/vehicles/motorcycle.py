from src.vehicles.base import Vehicle
from colorama import Fore, Style


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, region_spec: str) -> None:
        self.make = make
        self.model = model
        self.region_spec = region_spec

    def start_engine(self) -> None:
        msg = (
            f"{Fore.BLUE}{self.make} {self.model} ({self.region_spec}): "
            f"Мотор заведено{Style.RESET_ALL}"
        )
        print(msg)
