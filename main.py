from src.factories import EUVehicleFactory, USVehicleFactory

us_factory = USVehicleFactory()
vehicle1 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle1.start_engine()

eu_factory = EUVehicleFactory()
vehicle2 = eu_factory.create_car("Toyota", "Corolla")
vehicle2.start_engine()
