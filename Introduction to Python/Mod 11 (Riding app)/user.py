"""
User classes for the ride-sharing system.
Contains the base User class and its subclasses (Rider and Driver).
"""
from abc import ABC, abstractmethod

class User(ABC):
    """Abstract base class for all users in the system."""
    
    def __init__(self, name, email, nid):
        """
        Initialize a user with a name, email, and national ID.
        
        Args:
            name (str): The user's full name
            email (str): The user's email address
            nid (str): The user's national ID number
        """
        self.name = name
        self.email = email
        self.nid = nid
    
    @abstractmethod
    def display_profile(self):
        """Abstract method to display the user's profile."""
        pass


class Rider(User):
    """Rider class representing a user who can request rides."""
    
    def __init__(self, name, email, nid, current_location, initial_amount=0):
        """
        Initialize a rider with name, email, national ID, current location, and initial wallet amount.
        
        Args:
            name (str): The rider's full name
            email (str): The rider's email address
            nid (str): The rider's national ID number
            current_location (str): The rider's current location
            initial_amount (float, optional): Initial amount in the rider's wallet. Defaults to 0.
        """
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet_amount = initial_amount
        self.current_ride = None
        self.total_rides = 0
        self.rating = 5.0
        self.password = None  # For authentication
        self.favorite_locations = []
    
    def display_profile(self):
        """Display the rider's profile information."""
        print(f"\n=== Rider Profile ===")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"National ID: {self.nid}")
        print(f"Current Location: {self.current_location}")
        print(f"Wallet Balance: ${self.wallet_amount:.2f}")
        
    def load_cash(self, amount):
        """
        Add cash to the rider's wallet.
        
        Args:
            amount (float): Amount to add to the wallet
            
        Returns:
            float: New wallet balance
        """
        if amount <= 0:
            print("Amount must be positive")
            return self.wallet_amount
            
        self.wallet_amount += amount
        print(f"${amount:.2f} added to your wallet. New balance: ${self.wallet_amount:.2f}")
        return self.wallet_amount
    
    def update_location(self, current_location):
        """
        Update the rider's current location.
        
        Args:
            current_location (str): The rider's new location
        """
        self.current_location = current_location
        print(f"Location updated to: {self.current_location}")
    
    def request_ride(self, ride_sharing, destination):
        """
        Request a ride to a destination.
        
        Args:
            ride_sharing: The ride-sharing system to request the ride through
            destination (str): The destination location
            
        Returns:
            Ride_Request: The created ride request
        """
        from ride_request import Ride_Request
        
        # Create a ride request
        request = Ride_Request(self, destination)
        
        # Submit the request to the ride sharing system
        ride_sharing.process_ride_request(request)
        
        return request
    
    def show_current_ride(self):
        """Display details of the rider's current ride."""
        if self.current_ride:
            print("\n=== Current Ride Details ===")
            print(self.current_ride)
        else:
            print("You don't have any active rides.")


class Driver(User):
    """Driver class representing a user who can provide rides."""
    
    def __init__(self, name, email, nid, current_location):
        """
        Initialize a driver with name, email, national ID, and current location.
        
        Args:
            name (str): The driver's full name
            email (str): The driver's email address
            nid (str): The driver's national ID number
            current_location (str): The driver's current location
        """
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.available = True
        self.current_ride = None
        self.earnings = 0
        self.vehicle = None
        self.rating = 5.0
        self.completed_rides = 0
        self.password = None  # For authentication
        
    def display_profile(self):
        """Display the driver's profile information."""
        print(f"\n=== Driver Profile ===")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"National ID: {self.nid}")
        print(f"Current Location: {self.current_location}")
        print(f"Available: {'Yes' if self.available else 'No'}")
        print(f"Total Earnings: ${self.earnings:.2f}")
    
    def accept_ride(self, ride):
        """
        Accept a ride request and start the ride.
        
        Args:
            ride: The ride to accept
            
        Returns:
            bool: True if ride was successfully accepted, False otherwise
        """
        if not self.available:
            print("You are currently unavailable or already on a ride.")
            return False
            
        # Set this driver to the ride
        ride.set_driver(self)
        
        # Mark driver as unavailable
        self.available = False
        self.current_ride = ride
        
        # Start the ride
        ride.start_ride()
        
        print(f"Ride accepted. You are now en route to pick up {ride.rider.name}.")
        return True
    
    def update_location(self, current_location):
        """
        Update the driver's current location.
        
        Args:
            current_location (str): The driver's new location
        """
        self.current_location = current_location
        print(f"Location updated to: {self.current_location}")
    
    def complete_ride(self, amount):
        """
        Complete the current ride and add earnings.
        
        Args:
            amount (float): The fare amount for the completed ride
        """
        if self.current_ride:
            self.earnings += amount
            self.available = True
            self.current_ride = None
            print(f"\nRide completed. You earned ${amount:.2f}")
        else:
            print("No active ride to complete.")