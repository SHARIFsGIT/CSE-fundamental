"""
Ride_Sharing class for the ride-sharing system.
Main class that manages the entire ride-sharing system.
"""
from ride_matching import Ride_Matching
import random
import datetime
import time

class Ride_Sharing:
    """Class to manage the entire ride-sharing system."""
    
    def __init__(self, company_name):
        """
        Initialize a ride-sharing company with a specified name.
        
        Args:
            company_name (str): The name of the ride-sharing company
        """
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
        self.ride_requests = []
        self.ride_matcher = Ride_Matching([])
    
    def add_rider(self, rider):
        """
        Add a rider to the ride-sharing system.
        
        Args:
            rider: The rider to add
        """
        if rider not in self.riders:
            self.riders.append(rider)
            print(f"Rider {rider.name} added to {self.company_name}.")
    
    def add_driver(self, driver):
        """
        Add a driver to the ride-sharing system.
        
        Args:
            driver: The driver to add
        """
        if driver not in self.drivers:
            self.drivers.append(driver)
            self.ride_matcher.add_driver(driver)
            print(f"Driver {driver.name} added to {self.company_name}.")
    
    def process_ride_request(self, ride_request):
        """
        Process a ride request by finding a driver and creating a ride.
        
        Args:
            ride_request: The ride request to process
            
        Returns:
            Ride: The created ride if successful, None otherwise
        """
        # Store the request
        self.ride_requests.append(ride_request)
        
        print(f"\nProcessing ride request from {ride_request.rider.name}...")
        print(f"From: {ride_request.start_location}")
        print(f"To: {ride_request.end_location}")
        
        print("\nLooking for drivers...")
        time.sleep(3)  # Add a realistic delay
        
        # Find a driver
        driver, ride = self.ride_matcher.find_driver(ride_request)
        
        if not driver:
            print("No suitable driver found. Please try again later.")
            return None
        
        # Driver accepts the ride
        if driver.accept_ride(ride):
            # Mark the request as accepted
            ride_request.accept(driver)
            
            # Add the ride to our list of rides
            self.rides.append(ride)
            
            # Set the current ride for the rider
            ride_request.rider.current_ride = ride
            
            # Calculate estimated fare (more realistic)
            distance = random.uniform(1, 15)  # Random distance between 1-15 km
            base_fare = 5.0
            rate_per_km = driver.vehicle.rate if hasattr(driver, 'vehicle') else 2.0
            estimated_fare = base_fare + (distance * rate_per_km)
            
            # Check for surge pricing
            current_hour = datetime.datetime.now().hour
            if current_hour in [7, 8, 9, 17, 18, 19]:  # Rush hours
                surge_multiplier = random.uniform(1.2, 1.5)
                estimated_fare *= surge_multiplier
                print(f"Note: Surge pricing of {surge_multiplier:.1f}x is currently in effect.")
            
            print(f"Estimated fare: ${estimated_fare:.2f} for distance {distance:.1f} km")
            
            return ride
        
        return None
    
    def __repr__(self):
        """String representation of the ride-sharing company."""
        return (
            f"{self.company_name} Ride Sharing\n"
            f"Registered riders: {len(self.riders)}\n"
            f"Registered drivers: {len(self.drivers)}\n"
            f"Total rides completed: {len([r for r in self.rides if r.status == 'completed'])}"
        )