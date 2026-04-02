import logging

from src.factories import EUVehicleFactory, USVehicleFactory
from src.logger import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    configure_logging()
    logger.info("Демонстрація фабрик транспортних засобів.")

    us_factory = USVehicleFactory()
    vehicle1 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle1.start_engine()

    eu_factory = EUVehicleFactory()
    vehicle2 = eu_factory.create_car("Toyota", "Corolla")
    vehicle2.start_engine()


if __name__ == "__main__":
    main()
