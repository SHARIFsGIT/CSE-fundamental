"""
Driver UI for the ride-sharing system.
Provides a dashboard for drivers to manage rides.
"""
import os
import time

class DriverUI:
    """Class to handle the driver user interface."""
    
    def __init__(self, ride_sharing, driver):
        """
        Initialize the driver UI with a ride-sharing system and driver.
        
        Args:
            ride_sharing: The ride-sharing system to use
            driver: The driver using this interface
        """
        self.ride_sharing = ride_sharing
        self.driver = driver
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display the driver dashboard header."""
        self.clear_screen()
        print(f"\n{'=' * 50}")
        print(f"{self.ride_sharing.company_name} - DRIVER DASHBOARD")
        print(f"Hello, {self.driver.name}!")
        print(f"{'=' * 50}")
    
    def display_dashboard(self):
        """Display the main driver dashboard."""
        self.display_header()
        
        # Display total earnings
        print(f"\nTotal Earnings: ${self.driver.earnings:.2f}")
        
        # Display current location
        print(f"Current Location: {self.driver.current_location}")
        
        # Display availability status
        status = "Available" if self.driver.available else "Busy"
        print(f"Status: {status}")
        
        # Check if there's an active ride
        if self.driver.current_ride and self.driver.current_ride.status != 'completed':
            print("\n=== Current Ride Status ===")
            print(self.driver.current_ride)
        
        # Display menu options
        print("\n=== Driver Actions ===")
        
        if self.driver.available:
            print("1. Look for Ride Requests")
        else:
            print("1. Complete Current Ride")
            
        print("2. View Ride History")
        print("3. Update My Location")
        print("4. View My Profile")
        print("5. Logout")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            if self.driver.available:
                self.look_for_rides()
            else:
                self.complete_current_ride()
        elif choice == '2':
            self.view_ride_history()
        elif choice == '3':
            self.update_location()
        elif choice == '4':
            self.view_profile()
        elif choice == '5':
            return False
        else:
            input("Invalid choice. Press Enter to continue...")
        
        return True
    
    def look_for_rides(self):
        """Look for ride requests near the driver's location."""
        self.display_header()
        
        print("\n=== Looking for Ride Requests ===")
        
        # In a real app, we would show real ride requests
        # For this example, we'll simulate finding a ride request
        
        print("Searching for ride requests near your location...")
        time.sleep(2)  # Wait for 2 seconds
        
        # Check if there are any pending ride requests
        pending_requests = [r for r in self.ride_sharing.ride_requests 
                           if r.status == 'pending']
        
        if not pending_requests:
            print("\nNo ride requests available at the moment.")
            input("Press Enter to continue...")
            return
        
        # Get the first pending request
        request = pending_requests[0]
        
        print(f"\nFound ride request from {request.rider.name}")
        print(f"Pickup: {request.start_location}")
        print(f"Destination: {request.end_location}")
        
        # Ask if driver wants to accept
        accept = input("\nAccept this ride? (y/n): ")
        
        if accept.lower() != 'y':
            print("Ride request ignored.")
            input("Press Enter to continue...")
            return
        
        # Create a ride and assign the driver
        from ride import Ride
        ride = Ride(request.start_location, request.end_location)
        ride.rider = request.rider
        
        # Driver accepts the ride
        if self.driver.accept_ride(ride):
            # Mark the request as accepted
            request.accept(self.driver)
            
            # Add the ride to the system's list of rides
            self.ride_sharing.rides.append(ride)
            
            # Set the current ride for the rider
            request.rider.current_ride = ride
            
            print("\nRide accepted! You are now en route to the pickup location.")
        else:
            print("\nFailed to accept the ride.")
        
        input("Press Enter to continue...")
    
    def complete_current_ride(self):
        """Complete the current ride."""
        self.display_header()
        
        if not self.driver.current_ride or self.driver.current_ride.status == 'completed':
            print("\nYou don't have an active ride to complete.")
            input("Press Enter to continue...")
            return
        
        print("\n=== Complete Current Ride ===")
        print(self.driver.current_ride)
        
        # Confirm completion
        confirm = input("\nConfirm ride completion? (y/n): ")
        
        if confirm.lower() != 'y':
            print("Ride completion cancelled.")
            input("Press Enter to continue...")
            return
        
        # Calculate fare (in a real app, this would be calculated based on distance, time, etc.)
        import random
        fare = random.uniform(10, 50)
        
        # End the ride
        if self.driver.current_ride.end_ride(self.driver.current_ride.rider, fare):
            print("\nRide completed successfully!")
            print(f"You earned ${fare:.2f}")
            
            # Reset driver status
            self.driver.available = True
            self.driver.current_ride = None
        else:
            print("\nFailed to complete the ride.")
        
        input("Press Enter to continue...")
    
    def view_ride_history(self):
        """View the driver's ride history."""
        self.display_header()
        
        # Find all completed rides for this driver
        rides = [r for r in self.ride_sharing.rides 
                if r.driver == self.driver and r.status == 'completed']
        
        if not rides:
            print("\nYou haven't completed any rides yet.")
            input("Press Enter to continue...")
            return
        
        print("\n=== Your Ride History ===")
        
        for i, ride in enumerate(rides, 1):
            duration = ride.end_time - ride.start_time
            minutes = duration.total_seconds() / 60
            
            print(f"\nRide #{i}")
            print(f"Rider: {ride.rider.name}")
            print(f"From: {ride.start_location}")
            print(f"To: {ride.end_location}")
            print(f"Date: {ride.start_time.strftime('%Y-%m-%d')}")
            print(f"Duration: {minutes:.1f} minutes")
            print(f"Fare: ${ride.fare:.2f}")
        
        input("\nPress Enter to continue...")
    
    def update_location(self):
        """Update the driver's current location."""
        self.display_header()
        
        print("\n=== Update Your Location ===")
        print(f"Current location: {self.driver.current_location}")
        
        new_location = input("Enter your new location: ")
        
        if not new_location:
            print("Location cannot be empty.")
            input("Press Enter to continue...")
            return
        
        self.driver.update_location(new_location)
        input("Press Enter to continue...")
    
    def view_profile(self):
        """View the driver's profile."""
        self.display_header()
        
        print("\n=== My Profile ===")
        self.driver.display_profile()
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Run the driver UI main loop."""
        while self.display_dashboard():
            pass
        
        print("\nLogged out from Driver Dashboard.")