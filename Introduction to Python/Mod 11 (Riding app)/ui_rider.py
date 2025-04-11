"""
Rider UI for the ride-sharing system.
Provides a dashboard for riders to request and manage rides.
"""
import os
import time
import random
import datetime

class RiderUI:
    """Class to handle the rider user interface."""
    
    def __init__(self, ride_sharing, rider):
        """
        Initialize the rider UI with a ride-sharing system and rider.
        
        Args:
            ride_sharing: The ride-sharing system to use
            rider: The rider using this interface
        """
        self.ride_sharing = ride_sharing
        self.rider = rider
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display the rider dashboard header."""
        self.clear_screen()
        print(f"\n{'=' * 50}")
        print(f"{self.ride_sharing.company_name} - RIDER DASHBOARD")
        print(f"Hello, {self.rider.name}!")
        print(f"{'=' * 50}")
    
    def display_dashboard(self):
        """Display the main rider dashboard."""
        self.display_header()
        
        # Display wallet balance
        print(f"\nWallet Balance: ${self.rider.wallet_amount:.2f}")
        
        # Display current location
        print(f"Current Location: {self.rider.current_location}")
        
        # Check if there's an active ride
        if self.rider.current_ride and self.rider.current_ride.status != 'completed':
            print("\n=== Current Ride Status ===")
            print(self.rider.current_ride)
        
        # Display menu options
        print("\n=== Rider Actions ===")
        print("1. Request a Ride")
        print("2. View Ride History")
        print("3. Update My Location")
        print("4. Add Money to Wallet")
        print("5. View My Profile")
        print("6. Logout")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            self.request_ride()
        elif choice == '2':
            self.view_ride_history()
        elif choice == '3':
            self.update_location()
        elif choice == '4':
            self.add_money()
        elif choice == '5':
            self.view_profile()
        elif choice == '6':
            return False
        else:
            input("Invalid choice. Press Enter to continue...")
        
        return True
    
    def request_ride(self):
        """Request a new ride."""
        self.display_header()
        
        # Check if rider already has an active ride
        if self.rider.current_ride and self.rider.current_ride.status != 'completed':
            print("\nYou already have an active ride. Please complete it first.")
            input("Press Enter to continue...")
            return
        
        print("\n=== Request a Ride ===")
        
        # Get destination
        destination = input("Enter your destination: ")
        
        if not destination:
            print("Destination cannot be empty.")
            input("Press Enter to continue...")
            return
        
        # Confirm request
        print(f"\nRequesting ride from {self.rider.current_location} to {destination}")
        confirm = input("Confirm? (y/n): ")
        
        if confirm.lower() != 'y':
            print("Ride request cancelled.")
            input("Press Enter to continue...")
            return
        
        # Request the ride
        ride_request = self.rider.request_ride(self.ride_sharing, destination)
        
        if not ride_request:
            print("Failed to create ride request.")
            input("Press Enter to continue...")
            return
        
        # Simulating wait for driver
        time.sleep(2)  # Wait for 2 seconds
        
        # Check if ride was created successfully
        if self.rider.current_ride:
            print(f"\nRide created successfully!")
            print(f"Driver {self.rider.current_ride.driver.name} is coming to pick you up.")
            print(f"Vehicle: {self.rider.current_ride.driver.vehicle}")
            print(f"Driver rating: {self.rider.current_ride.driver.rating:.1f}/5.0 ({self.rider.current_ride.driver.completed_rides} rides)")
            print(f"Estimated arrival time: {random.randint(3, 4)} minutes")
            
            # Simulate ride progress in a more realistic way
            print("\n=== Ride in Progress ===")
            
            # Calculate estimated time based on fictional distance
            distance = random.uniform(2.5, 20.0)  # km
            speed = random.uniform(30, 50)  # km/h
            time_minutes = (distance / speed) * 60
            
            # Format estimated time of arrival
            now = datetime.datetime.now()
            arrival = now + datetime.timedelta(minutes=time_minutes)
            
            print(f"Distance: {distance:.1f} km")
            print(f"Estimated time of arrival: {arrival.strftime('%H:%M')}")
            
            # Show ride progress updates
            total_steps = 4
            for step in range(total_steps):
                progress_percent = (step + 1) / total_steps * 100
                
                if step == 0:
                    print("\nDriver is on the way to pickup location...")
                elif step == 1:
                    print("\nYou have been picked up! Heading to destination...")
                elif step == 2:
                    print("\nNearing destination...")
                elif step == 3:
                    print("\nArrived at destination!")
                
                # Progress bar
                progress_bar = "█" * int(progress_percent / 10) + "░" * (10 - int(progress_percent / 10))
                print(f"[{progress_bar}] {progress_percent:.0f}%")
                
                time.sleep(2.5)  # Wait between updates
            
            # Calculate a realistic fare based on distance and base fare
            base_fare = 5.0
            rate_per_km = self.rider.current_ride.driver.vehicle.rate
            fare = base_fare + (distance * rate_per_km)
            
            # Add surge pricing randomly (10% chance)
            if random.random() < 0.1:
                surge_multiplier = random.uniform(1.2, 1.8)
                fare *= surge_multiplier
                print(f"\nSurge pricing applied (x{surge_multiplier:.1f})")
            
            # End the ride
            self.rider.current_ride.end_ride(self.rider, fare)
            
            print("\nRide completed!")
        else:
            print("\nNo drivers available. Please try again later.")
        
        input("Press Enter to continue...")
    
    def view_ride_history(self):
        """View the rider's ride history."""
        self.display_header()
        
        # Find all rides for this rider
        rides = [r for r in self.ride_sharing.rides if r.rider == self.rider and r.status == 'completed']
        
        if not rides:
            print("\nYou haven't taken any rides yet.")
            input("Press Enter to continue...")
            return
        
        print("\n=== Your Ride History ===")
        
        for i, ride in enumerate(rides, 1):
            duration = ride.end_time - ride.start_time
            minutes = duration.total_seconds() / 60
            
            print(f"\nRide #{i}")
            print(f"From: {ride.start_location}")
            print(f"To: {ride.end_location}")
            print(f"Driver: {ride.driver.name if ride.driver else 'Unknown'}")
            print(f"Date: {ride.start_time.strftime('%Y-%m-%d')}")
            print(f"Duration: {minutes:.1f} minutes")
            print(f"Fare: ${ride.fare:.2f}")
        
        input("\nPress Enter to continue...")
    
    def update_location(self):
        """Update the rider's current location."""
        self.display_header()
        
        print("\n=== Update Your Location ===")
        print(f"Current location: {self.rider.current_location}")
        
        new_location = input("Enter your new location: ")
        
        if not new_location:
            print("Location cannot be empty.")
            input("Press Enter to continue...")
            return
        
        self.rider.update_location(new_location)
        input("Press Enter to continue...")
    
    def add_money(self):
        """Add money to the rider's wallet."""
        self.display_header()
        
        print("\n=== Add Money to Wallet ===")
        print(f"Current balance: ${self.rider.wallet_amount:.2f}")
        
        try:
            amount = float(input("Enter amount to add: $"))
            
            if amount <= 0:
                print("Amount must be greater than zero.")
                input("Press Enter to continue...")
                return
            
            self.rider.load_cash(amount)
        except ValueError:
            print("Invalid amount. Please enter a number.")
        
        input("Press Enter to continue...")
    
    def view_profile(self):
        """View the rider's profile."""
        self.display_header()
        
        print("\n=== My Profile ===")
        self.rider.display_profile()
        
        input("\nPress Enter to continue...")
    
    def run(self):
        """Run the rider UI main loop."""
        while self.display_dashboard():
            pass
        
        print("\nLogged out from Rider Dashboard.")