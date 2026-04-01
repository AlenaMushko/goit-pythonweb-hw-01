from src.factories.vehicle_factory import VehicleFactory
from src.vehicles.car import Car
from src.vehicles.motorcycle import Motorcycle


class USVehicleFactory(VehicleFactory):
    _SPEC = "US Spec"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self._SPEC)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self._SPEC)
