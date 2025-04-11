"""
Main entry point for the ride-sharing system.
Handles user authentication, registration, and redirects to appropriate dashboards.
"""
import os
import time
import random
import string
from getpass import getpass

# Import our modules
from ride_sharing import Ride_Sharing
from user import Rider, Driver
from vehicle import Car, Bike
from ui_admin import AdminUI
from ui_rider import RiderUI
from ui_driver import DriverUI

# Global ride sharing system
ride_sharing = None

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome_message():
    """Display the welcome message and app title."""
    clear_screen()
    print("\n" + "=" * 50)
    print(f"{'RIDE SHARING SYSTEM':^50}")
    print("=" * 50)

def create_demo_data():
    """Create demo data for testing the app."""
    # Create the ride sharing company
    global ride_sharing
    ride_sharing = Ride_Sharing("Quickride")
    
    # Create some riders
    riders = [
        Rider("John Doe", "john@example.com", "ID123", "Downtown", 100),
        Rider("Jane Smith", "jane@example.com", "ID456", "Uptown", 150),
        Rider("Bob Johnson", "bob@example.com", "ID789", "Midtown", 75)
    ]
    
    # Create some drivers with different vehicle types and rates
    drivers = [
        Driver("Alice Williams", "alice@example.com", "ID321", "Downtown"),
        Driver("Charlie Brown", "charlie@example.com", "ID654", "Uptown"),
        Driver("Dave Miller", "dave@example.com", "ID987", "Midtown")
    ]
    
    # Create some vehicles and assign them to drivers
    drivers[0].vehicle = Car("Sedan", "ABC123", 2.5)
    drivers[1].vehicle = Car("SUV", "DEF456", 3.0)
    drivers[2].vehicle = Bike("Scooter", "GHI789", 1.5)
    
    # Set earnings and ratings for more realistic data
    drivers[0].earnings = 325.75
    drivers[0].rating = 4.8
    drivers[0].completed_rides = 47
    
    drivers[1].earnings = 512.25
    drivers[1].rating = 4.6
    drivers[1].completed_rides = 72
    
    drivers[2].earnings = 187.50
    drivers[2].rating = 4.9
    drivers[2].completed_rides = 25
    
    # Set ride history for riders
    riders[0].total_rides = 15
    riders[0].rating = 4.7
    
    riders[1].total_rides = 28
    riders[1].rating = 4.9
    
    riders[2].total_rides = 8
    riders[2].rating = 4.5
    
    # Add riders and drivers to the system
    for rider in riders:
        ride_sharing.add_rider(rider)
    
    for driver in drivers:
        ride_sharing.add_driver(driver)
    
    return riders, drivers

def login_menu():
    """Display the login menu and handle user selection."""
    display_welcome_message()
    
    print("\nWelcome to the RideShare Dashboard!")
    print("====================================")
    print("Please choose from the options below:\n")

    print("Dashboard")
    print("1. Admin")
    print("2. Rider")
    print("3. Driver")

    print("\nNew registration")
    print("4. Rider")
    print("5. Driver")

    print("\n6. Exit")

    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        return 'admin_login'
    elif choice == '2':
        return 'rider_login'
    elif choice == '3':
        return 'driver_login'
    elif choice == '4':
        return 'rider_register'
    elif choice == '5':
        return 'driver_register'
    elif choice == '6':
        return 'exit'
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        return None

def authenticate_user(role):
    """
    Authenticate a user based on their role.
    
    Args:
        role (str): The user's role ('rider' or 'driver')
        
    Returns:
        User or None: The authenticated user, or None if authentication failed
    """
    display_welcome_message()
    
    print(f"\n{role.upper()} LOGIN")
    email = input("Email: ")
    password = getpass("Password: ")
    
    # In a real app, we would hash and verify the password
    # For this demo, we'll just check if the email exists
    
    if role == 'rider':
        for rider in ride_sharing.riders:
            if rider.email == email:
                # Check if password matches
                if rider.password == password:
                    print("\nLogin successful!")
                    time.sleep(1)
                    return rider
    elif role == 'driver':
        for driver in ride_sharing.drivers:
            if driver.email == email:
                # Check if password matches
                if driver.password == password:
                    print("\nLogin successful!")
                    time.sleep(1)
                    return driver
    
    print("Authentication failed. Invalid email or password.")
    time.sleep(2)
    return None

def register_user(role):
    """
    Register a new user based on their role.
    
    Args:
        role (str): The user's role ('rider' or 'driver')
        
    Returns:
        User or None: The newly registered user, or None if registration failed
    """
    display_welcome_message()
    
    print(f"\nREGISTER AS {role.upper()}")
    
    # Get user details
    name = input("Full Name: ")
    if not name:
        print("Name cannot be empty.")
        time.sleep(2)
        return None
    
    email = input("Email: ")
    if not email or '@' not in email:
        print("Please enter a valid email.")
        time.sleep(2)
        return None
    
    # Check if email already exists
    for user in ride_sharing.riders + ride_sharing.drivers:
        if user.email == email:
            print("Email already registered. Please use a different email.")
            time.sleep(2)
            return None
    
    # Generate a random national ID for demo purposes
    nid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
    
    location = input("Current Location: ")
    if not location:
        print("Location cannot be empty.")
        time.sleep(2)
        return None
    
    password = getpass("Create Password (must be 6 characters): ")
    if not password or len(password) < 6:
        print("Password must be at least 6 characters long.")
        time.sleep(2)
        return None
    
    confirm_password = getpass("Confirm Password (must be matched): ")
    if password != confirm_password:
        print("Passwords do not match.")
        time.sleep(2)
        return None
    
    # Create new user based on role
    if role == 'rider':
        user = Rider(name, email, nid, location, 0)
        user.password = password  # In a real app, we would hash this
        ride_sharing.add_rider(user)
    else:  # driver
        user = Driver(name, email, nid, location)
        user.password = password  # In a real app, we would hash this
        
        # For drivers, we need vehicle information
        print("\nVehicle Information:")
        vehicle_type = input("Vehicle Type (Car/Bike): ").capitalize()
        
        if vehicle_type not in ['Car', 'Bike']:
            print("Invalid vehicle type. Please choose Car or Bike.")
            time.sleep(2)
            return None
        
        license_plate = input("License Plate: ")
        if not license_plate:
            print("License plate cannot be empty.")
            time.sleep(2)
            return None
        
        try:
            rate = float(input("Rate per km ($): "))
            if rate <= 0:
                raise ValueError
        except ValueError:
            print("Please enter a valid rate.")
            time.sleep(2)
            return None
        
        # Create and assign vehicle
        if vehicle_type == 'Car':
            user.vehicle = Car(vehicle_type, license_plate, rate)
        else:
            user.vehicle = Bike(vehicle_type, license_plate, rate)
        
        ride_sharing.add_driver(user)
    
    print("\nRegistration successful! You can now log in with your email and password.")
    time.sleep(2)
    return user

def main():
    """Main function to run the ride-sharing system."""
    # Create demo data
    global ride_sharing
    create_demo_data()
    
    while True:
        option = login_menu()
        
        if option == 'exit':
            break
        elif option == 'admin_login':
            # For admin, just use a simple login
            display_welcome_message()
            print("\nADMIN LOGIN")
            username = input("Username: ")
            password = getpass("Password (enter 'admin' to login): ")
            
            if username and password == 'admin':
                # Run the admin dashboard
                admin_ui = AdminUI(ride_sharing)
                admin_ui.run()
            else:
                print("Admin authentication failed.")
                time.sleep(2)
        elif option == 'rider_login':
            rider = authenticate_user('rider')
            if rider:
                # Run the rider dashboard
                rider_ui = RiderUI(ride_sharing, rider)
                rider_ui.run()
        elif option == 'driver_login':
            driver = authenticate_user('driver')
            if driver:
                # Run the driver dashboard
                driver_ui = DriverUI(ride_sharing, driver)
                driver_ui.run()
        elif option == 'rider_register':
            register_user('rider')
        elif option == 'driver_register':
            register_user('driver')
    
    print("\nThank you for using the Ride Sharing System!")

if __name__ == "__main__":
    main()