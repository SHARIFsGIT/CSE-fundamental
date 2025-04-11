"""
Ride class for the ride-sharing system.
Handles the actual ride from start to end, including payment processing.
"""
import datetime

class Ride:
    """Class to represent a ride in the system."""
    
    def __init__(self, start_location, end_location):
        """
        Initialize a ride with start and end locations.
        
        Args:
            start_location (str): The pickup location for the ride
            end_location (str): The destination location for the ride
        """
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.fare = 0
        self.status = "created"  # possible states: created, ongoing, completed, cancelled
    
    def set_driver(self, driver):
        """
        Assign a driver to the ride.
        
        Args:
            driver: The driver to assign to this ride
        """
        self.driver = driver
        self.status = "assigned"
        print(f"Driver {driver.name} assigned to the ride.")
    
    def start_ride(self):
        """Mark the start time of the ride."""
        if not self.driver:
            print("Cannot start ride: No driver assigned.")
            return False
            
        self.start_time = datetime.datetime.now()
        self.status = "ongoing"
        print(f"\nRide started at {self.start_time.strftime('%H:%M:%S')}.")
        return True
    
    def end_ride(self, rider, amount):
        """
        Mark the end time of the ride and process payment.
        
        Args:
            rider: The rider who requested this ride
            amount (float): The fare amount to be paid
            
        Returns:
            bool: True if payment processed successfully, False otherwise
        """
        if self.status != "ongoing":
            print("Cannot end ride: Ride is not ongoing.")
            return False
            
        self.rider = rider
        self.end_time = datetime.datetime.now()
        self.fare = amount
        
        # Process payment
        if rider.wallet_amount < amount:
            print("Payment failed: Insufficient funds in wallet.")
            return False
            
        rider.wallet_amount -= amount
        self.status = "completed"
        
        # Update driver earnings if we have a driver
        if self.driver:
            self.driver.complete_ride(amount)
        
        duration = self.end_time - self.start_time
        minutes = duration.total_seconds() / 60
        
        print(f"Ride completed at {self.end_time.strftime('%H:%M:%S')}.")
        print(f"Duration: {minutes:.1f} minutes")
        print(f"Fare: ${self.fare:.2f}")
        print(f"Payment processed successfully.")
        
        return True
    
    def __repr__(self):
        """String representation of the ride."""
        status_str = f"Status: {self.status.upper()}"
        
        if self.start_time:
            start_time_str = f"Started: {self.start_time.strftime('%H:%M:%S')}"
        else:
            start_time_str = "Not started yet"
            
        if self.end_time:
            end_time_str = f"Ended: {self.end_time.strftime('%H:%M:%S')}"
            duration = self.end_time - self.start_time
            minutes = duration.total_seconds() / 60
            duration_str = f"Duration: {minutes:.1f} minutes"
            fare_str = f"Fare: ${self.fare:.2f}"
        else:
            end_time_str = "Not completed yet"
            duration_str = ""
            fare_str = "Fare: To be calculated"
        
        driver_str = f"Driver: {self.driver.name}" if self.driver else "No driver assigned yet"
        
        return (
            f"\nRide: {self.start_location} → {self.end_location}\n"
            f"{status_str}\n"
            f"{driver_str}\n"
            f"{start_time_str}\n"
            f"{end_time_str}\n"
            f"{duration_str}\n"
            f"{fare_str}"
        )