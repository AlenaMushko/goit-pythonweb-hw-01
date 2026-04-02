import logging

from src.vehicles.base import Vehicle

logger = logging.getLogger(__name__)


class Car(Vehicle):
    def __init__(self, make: str, model: str, region_spec: str) -> None:
        self.make = make
        self.model = model
        self.region_spec = region_spec

    def start_engine(self) -> None:
        logger.info(
            "%s %s (%s): Двигун запущено",
            self.make,
            self.model,
            self.region_spec,
        )
