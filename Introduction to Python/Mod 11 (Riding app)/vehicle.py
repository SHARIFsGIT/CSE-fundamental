"""
Vehicle classes for the ride-sharing system.
Contains the base Vehicle class and its subclasses (Car and Bike).
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for all vehicles in the system."""
    
    def __init__(self, vehicle_type, license_plate, rate):
        """
        Initialize a vehicle with type, license plate, and rate.
        
        Args:
            vehicle_type (str): The type of vehicle
            license_plate (str): The vehicle's license plate number
            rate (float): The per-kilometer rate for this vehicle
        """
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.available = True
    
    @abstractmethod
    def start_drive(self):
        """Abstract method to start driving the vehicle."""
        pass
    
    def __str__(self):
        """String representation of the vehicle."""
        return f"{self.vehicle_type} (License: {self.license_plate}, Rate: ${self.rate:.2f}/km)"


class Car(Vehicle):
    """Car subclass of Vehicle."""
    
    def __init__(self, vehicle_type, license_plate, rate):
        """
        Initialize a car with type, license plate, and rate.
        
        Args:
            vehicle_type (str): The type of car (e.g., "Sedan", "SUV")
            license_plate (str): The car's license plate number
            rate (float): The per-kilometer rate for this car
        """
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        """Mark the car as unavailable for driving."""
        self.available = False
        print(f"Starting drive with car: {self.vehicle_type} (License: {self.license_plate})")


class Bike(Vehicle):
    """Bike subclass of Vehicle."""
    
    def __init__(self, vehicle_type, license_plate, rate):
        """
        Initialize a bike with type, license plate, and rate.
        
        Args:
            vehicle_type (str): The type of bike (e.g., "Scooter", "Motorcycle")
            license_plate (str): The bike's license plate number
            rate (float): The per-kilometer rate for this bike
        """
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        """Mark the bike as unavailable for driving."""
        self.available = False
        print(f"Starting drive with bike: {self.vehicle_type} (License: {self.license_plate})")