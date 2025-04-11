"""
Admin UI for the ride-sharing system.
Provides a dashboard for administrators to manage the system.
"""
import os
from tabulate import tabulate

class AdminUI:
    """Class to handle the admin user interface."""
    
    def __init__(self, ride_sharing):
        """
        Initialize the admin UI with a ride-sharing system.
        
        Args:
            ride_sharing: The ride-sharing system to manage
        """
        self.ride_sharing = ride_sharing
    
    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        """Display the admin dashboard header."""
        self.clear_screen()
        print(f"\n{'=' * 50}")
        print(f"{self.ride_sharing.company_name} - ADMIN DASHBOARD")
        print(f"{'=' * 50}")
    
    def display_dashboard(self):
        """Display the main admin dashboard."""
        self.display_header()
        
        # Display system statistics
        print("\n=== System Statistics ===")
        print(f"Total Riders: {len(self.ride_sharing.riders)}")
        print(f"Total Drivers: {len(self.ride_sharing.drivers)}")
        
        completed_rides = [r for r in self.ride_sharing.rides if r.status == 'completed']
        ongoing_rides = [r for r in self.ride_sharing.rides if r.status == 'ongoing']
        
        print(f"Completed Rides: {len(completed_rides)}")
        print(f"Ongoing Rides: {len(ongoing_rides)}")
        
        # Display menu options
        print("\n=== Admin Actions ===")
        print("1. View All Riders")
        print("2. View All Drivers")
        print("3. View Active Rides")
        print("4. View Ride History")
        print("5. Logout")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            self.view_all_riders()
        elif choice == '2':
            self.view_all_drivers()
        elif choice == '3':
            self.view_active_rides()
        elif choice == '4':
            self.view_ride_history()
        elif choice == '5':
            return False
        else:
            input("Invalid choice. Press Enter to continue...")
        
        return True
    
    def view_all_riders(self):
        """Display all riders registered in the system."""
        self.display_header()
        
        if not self.ride_sharing.riders:
            print("\nNo riders registered in the system.")
            input("Press Enter to continue...")
            return
        
        print("\n=== All Registered Riders ===")
        
        # Prepare data for tabular display
        headers = ["Name", "Email", "Location", "Wallet Balance"]
        data = []
        
        for rider in self.ride_sharing.riders:
            data.append([
                rider.name,
                rider.email,
                rider.current_location,
                f"${rider.wallet_amount:.2f}"
            ])
        
        print(tabulate(data, headers=headers, tablefmt="grid"))
        input("Press Enter to continue...")
    
    def view_all_drivers(self):
        """Display all drivers registered in the system."""
        self.display_header()
        
        if not self.ride_sharing.drivers:
            print("\nNo drivers registered in the system.")
            input("Press Enter to continue...")
            return
        
        print("\n=== All Registered Drivers ===")
        
        # Prepare data for tabular display
        headers = ["Name", "Email", "Location", "Available", "Earnings"]
        data = []
        
        for driver in self.ride_sharing.drivers:
            data.append([
                driver.name,
                driver.email,
                driver.current_location,
                "Yes" if driver.available else "No",
                f"${driver.earnings:.2f}"
            ])
        
        print(tabulate(data, headers=headers, tablefmt="grid"))
        input("Press Enter to continue...")
    
    def view_active_rides(self):
        """Display all active rides in the system."""
        self.display_header()
        
        ongoing_rides = [r for r in self.ride_sharing.rides if r.status == 'ongoing']
        
        if not ongoing_rides:
            print("\nNo active rides at the moment.")
            input("Press Enter to continue...")
            return
        
        print("\n=== Active Rides ===")
        
        # Prepare data for tabular display
        headers = ["Rider", "Driver", "From", "To", "Start Time"]
        data = []
        
        for ride in ongoing_rides:
            data.append([
                ride.rider.name,
                ride.driver.name if ride.driver else "N/A",
                ride.start_location,
                ride.end_location,
                ride.start_time.strftime('%H:%M:%S') if ride.start_time else "N/A"
            ])
        
        print(tabulate(data, headers=headers, tablefmt="grid"))
        input("Press Enter to continue...")
    
    def view_ride_history(self):
        """Display the history of all completed rides."""
        self.display_header()
        
        completed_rides = [r for r in self.ride_sharing.rides if r.status == 'completed']
        
        if not completed_rides:
            print("\nNo completed rides yet.")
            input("Press Enter to continue...")
            return
        
        print("\n=== Ride History ===")
        
        # Prepare data for tabular display
        headers = ["Rider", "Driver", "From", "To", "Duration", "Fare"]
        data = []
        
        for ride in completed_rides:
            duration = ride.end_time - ride.start_time
            minutes = duration.total_seconds() / 60
            
            data.append([
                ride.rider.name,
                ride.driver.name if ride.driver else "N/A",
                ride.start_location,
                ride.end_location,
                f"{minutes:.1f} min",
                f"${ride.fare:.2f}"
            ])
        
        print(tabulate(data, headers=headers, tablefmt="grid"))
        input("Press Enter to continue...")
    
    def run(self):
        """Run the admin UI main loop."""
        while self.display_dashboard():
            pass
        
        print("\nLogged out from Admin Dashboard.")