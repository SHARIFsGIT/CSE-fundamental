"""
Ride_Matching class for the ride-sharing system.
Responsible for matching ride requests with available drivers.
"""
import random
from ride import Ride

class Ride_Matching:
    """Class to match ride requests with available drivers."""
    
    def __init__(self, drivers):
        """
        Initialize a ride matcher with available drivers.
        
        Args:
            drivers (list): List of available drivers
        """
        self.drivers = drivers
    
    def find_driver(self, ride_request):
        """
        Match a driver to a ride request based on location and availability.
        
        Args:
            ride_request: The ride request to match a driver to
            
        Returns:
            tuple: (driver, ride) if matched, (None, None) otherwise
        """
        # Get the rider's location
        pickup_location = ride_request.start_location
        
        # Find available drivers nearby (simplified version)
        available_drivers = [driver for driver in self.drivers if driver.available]
        
        if not available_drivers:
            print("No drivers available at the moment.")
            return None, None
        
        # In a real app, we would use distance calculation algorithms here
        # For this implementation, we'll use a more realistic approach
        
        # First, filter drivers by proximity (simulate this with a probability)
        nearby_drivers = []
        for driver in available_drivers:
            # Simulate proximity check - drivers are considered "nearby" with this probability
            if random.random() < 0.6:  
                nearby_drivers.append(driver)
        
        if not nearby_drivers:
            # If no drivers are nearby, use all available drivers
            nearby_drivers = available_drivers
        
        # Calculate a "score" for each driver based on rating and proximity
        # Higher score = better match
        driver_scores = []
        for driver in nearby_drivers:
            # Simulated distance to pickup (1-10 km)
            distance = random.uniform(1, 10)
            
            # Factors that influence driver selection:
            # - Rating (higher is better)
            # - Distance to pickup (lower is better)
            # - Vehicle type suitability
            rating_factor = driver.rating / 5.0  # Normalized rating (0-1)
            distance_factor = 1 - (distance / 10)  # Normalized distance (0-1)
            
            # Calculate overall score
            score = (0.5 * rating_factor) + (0.5 * distance_factor)
            
            driver_scores.append((driver, score, distance))
        
        # Sort by score (highest first)
        driver_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Select the best driver
        selected_driver, _, distance_to_pickup = driver_scores[0]
        
        # Create a new ride
        ride = Ride(ride_request.start_location, ride_request.end_location)
        ride.rider = ride_request.rider
        
        # Store pickup distance for realistic ETA calculation
        ride.pickup_distance = distance_to_pickup
        
        print(f"Found driver {selected_driver.name} for the ride.")
        print(f"Driver is approximately {distance_to_pickup:.1f} km away.")
        print(f"Driver rating: {selected_driver.rating:.1f}/5.0 ({selected_driver.completed_rides} completed rides)")
        
        return selected_driver, ride
    
    def add_driver(self, driver):
        """
        Add a driver to the list of available drivers.
        
        Args:
            driver: The driver to add
        """
        if driver not in self.drivers:
            self.drivers.append(driver)
            print(f"Driver {driver.name} added to the pool.")
    
    def remove_driver(self, driver):
        """
        Remove a driver from the list of available drivers.
        
        Args:
            driver: The driver to remove
        """
        if driver in self.drivers:
            self.drivers.remove(driver)
            print(f"Driver {driver.name} removed from the pool.")