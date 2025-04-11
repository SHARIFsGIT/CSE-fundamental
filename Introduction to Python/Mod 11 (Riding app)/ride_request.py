"""
Ride_Request class for the ride-sharing system.
Handles ride requests from riders.
"""
import datetime

class Ride_Request:
    """Class to represent a ride request in the system."""
    
    def __init__(self, rider, end_location):
        """
        Initialize a ride request with a rider and destination.
        
        Args:
            rider: The rider requesting the ride
            end_location (str): The destination location
        """
        self.rider = rider
        self.start_location = rider.current_location
        self.end_location = end_location
        self.request_time = datetime.datetime.now()
        self.status = "pending"  # possible states: pending, accepted, declined, expired
    
    def accept(self, driver):
        """
        Mark the ride request as accepted by a driver.
        
        Args:
            driver: The driver who accepted the request
            
        Returns:
            bool: True if successfully accepted, False otherwise
        """
        if self.status != "pending":
            print(f"Cannot accept request: Request is {self.status}.")
            return False
            
        self.status = "accepted"
        print(f"Ride request accepted by driver {driver.name}.")
        return True
    
    def decline(self):
        """Mark the ride request as declined."""
        if self.status != "pending":
            print(f"Cannot decline request: Request is {self.status}.")
            return False
            
        self.status = "declined"
        print("Ride request declined.")
        return True
    
    def expire(self):
        """Mark the ride request as expired."""
        if self.status != "pending":
            return False
            
        self.status = "expired"
        print("Ride request expired.")
        return True
    
    def __repr__(self):
        """String representation of the ride request."""
        time_str = self.request_time.strftime('%H:%M:%S')
        return (
            f"Ride Request [{self.status.upper()}]\n"
            f"Rider: {self.rider.name}\n"
            f"From: {self.start_location}\n"
            f"To: {self.end_location}\n"
            f"Requested at: {time_str}"
        )