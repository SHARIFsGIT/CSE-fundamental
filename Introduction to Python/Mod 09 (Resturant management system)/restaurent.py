# -------------------- Restaurant Class --------------------
"""
This module defines the Restaurant class for the restaurant management system.
The Restaurant class is the central component that maintains menu, employees, and orders.
"""
from menu import Menu
from datetime import datetime, timedelta
import csv
import os

class Restaurant:
    """
    # Class: Restaurant
    # Purpose: Represents a restaurant with name, employees, menu, and orders
    #
    # Properties:
    # - name: Name of the restaurant
    # - employees: List of employees
    # - menu: Menu object containing food items
    # - orders: List of orders
    # - revenue: Total revenue
    # - address: Restaurant address (new)
    # - phone: Restaurant phone number (new)
    # - opening_hours: Dictionary of opening hours (new)
    # - tables: List of tables (new)
    """
    def __init__(self, name, address="", phone=""):
        """
        # Constructor
        # Initializes a new instance of the Restaurant class
        #
        # Parameters:
        # - name: The name of the restaurant
        # - address: The address of the restaurant (default: "")
        # - phone: The phone number of the restaurant (default: "")
        """
        # Instance attributes/properties
        self.name = name
        self.address = address
        self.phone = phone
        self.employees = []
        self.menu = Menu()
        self.orders = []
        self.revenue = 0.0
        self.expenses = 0.0
        self.tables = []  # List of tables in the restaurant
        self.reservations = []  # List of reservations
        
        # Initialize default opening hours (24-hour format)
        self.opening_hours = {
            "Monday": {"open": "09:00", "close": "22:00"},
            "Tuesday": {"open": "09:00", "close": "22:00"},
            "Wednesday": {"open": "09:00", "close": "22:00"},
            "Thursday": {"open": "09:00", "close": "22:00"},
            "Friday": {"open": "09:00", "close": "23:00"},
            "Saturday": {"open": "10:00", "close": "23:00"},
            "Sunday": {"open": "10:00", "close": "21:00"}
        }
        
        # Create a data directory for the restaurant
        self.data_dir = f"data/{self.name.replace(' ', '_')}"
        self._initialize_data_storage()

    def _initialize_data_storage(self):
        """
        # Private Method: _initialize_data_storage
        # Creates the necessary directories and files for data storage
        """
        # Create data directory if it doesn't exist
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir, exist_ok=True)
            # This simulates database initialization
            print(f"Database initialized for {self.name}")
        
    def add_employee(self, employee):
        """
        # Method: add_employee
        # Adds an employee to the restaurant
        #
        # Parameters:
        # - employee: The Employee object to add
        #
        # Returns:
        # - bool: True if added successfully, False if employee already exists
        """
        # Check if employee with same name already exists
        for emp in self.employees:
            if emp.name == employee.name:
                print(f"Employee {employee.name} already exists.")
                return False
                
        self.employees.append(employee)
        print(f"{employee.name} has joined as {employee.job_title}.")
        
        # Simulate database operation
        self._save_employee_to_database(employee)
        return True

    def _save_employee_to_database(self, employee):
        """
        # Private Method: _save_employee_to_database
        # Simulates saving an employee to a database
        #
        # Parameters:
        # - employee: The Employee object to save
        """
        # In a real system, this would interact with a database
        # For now, we'll simulate it by printing a message
        print(f"Database: Employee {employee.name} saved to database")
    
    def remove_employee(self, employee_name):
        """
        # Method: remove_employee
        # Removes an employee from the restaurant by name
        #
        # Parameters:
        # - employee_name: The name of the employee to remove
        #
        # Returns:
        # - bool: True if removed successfully, False if employee not found
        """
        for i, employee in enumerate(self.employees):
            if employee.name.lower() == employee_name.lower():
                removed_employee = self.employees.pop(i)
                print(f"{removed_employee.name} has been removed from the employee list.")
                
                # Simulate database operation
                self._delete_employee_from_database(employee_name)
                return True
                
        print(f"No employee named {employee_name} was found.")
        return False
        
    def _delete_employee_from_database(self, employee_name):
        """
        # Private Method: _delete_employee_from_database
        # Simulates deleting an employee from a database
        #
        # Parameters:
        # - employee_name: The name of the employee to delete
        """
        # In a real system, this would interact with a database
        print(f"Database: Employee {employee_name} deleted from database")

    def find_employee(self, employee_name):
        """
        # Method: find_employee
        # Finds an employee by name
        #
        # Parameters:
        # - employee_name: The name of the employee to find
        #
        # Returns:
        # - Employee: The found employee or None if not found
        """
        for employee in self.employees:
            if employee.name.lower() == employee_name.lower():
                return employee
        return None

    def show_all_employees(self):
        """
        # Method: show_all_employees
        # Displays all employees with their details
        """
        if not self.employees:
            print("No employees currently hired.")
            return

        print("\n" + "="*80)
        print(f"{'Name':<20}{'Job Title':<20}{'Salary':^10}{'Contact':<20}{'Age':^5}{'Email':<30}")
        print("-"*80)
        for emp in self.employees:
            print(f"{emp.name:<20}{emp.job_title:<20}${emp.salary:<9.2f}{emp.phone:<20}{emp.age:^5}{emp.email:<30}")
        print("="*80 + "\n")
        
    def add_food_item(self, food_item):
        """
        # Method: add_food_item
        # Adds a food item to the restaurant's menu
        #
        # Parameters:
        # - food_item: The FoodItem object to add
        #
        # Returns:
        # - bool: True if added successfully, False otherwise
        """
        return self.menu.add_item(food_item)
        
    def remove_food_item(self, item_name):
        """
        # Method: remove_food_item
        # Removes a food item from the restaurant's menu
        #
        # Parameters:
        # - item_name: The name of the item to remove
        #
        # Returns:
        # - bool: True if removed successfully, False if not found
        """
        return self.menu.remove_item(item_name)
        
    def find_food_item(self, item_name):
        """
        # Method: find_food_item
        # Finds a food item by name
        #
        # Parameters:
        # - item_name: The name of the item to find
        #
        # Returns:
        # - FoodItem: The found item or None if not found
        """
        return self.menu.find_item(item_name)
        
    def display_menu(self):
        """
        # Method: display_menu
        # Displays the restaurant's menu
        """
        print(f"\n{self.name}'s Menu")
        self.menu.display_menu()
        
    def process_order(self, order):
        """
        # Method: process_order
        # Processes a placed order
        #
        # Parameters:
        # - order: The Order object to process
        #
        # Returns:
        # - bool: True if processed successfully, False otherwise
        """
        if order.status != "Placed":
            print("This order has not been placed yet.")
            return False
            
        # Deduct items from inventory
        for item, quantity in order.items.items():
            item.update_quantity(-quantity)
            
        # Add order to restaurant's orders
        self.orders.append(order)
        
        # Update revenue (only when processed, not when delivered)
        self.revenue += order.calculate_total_price()
        
        # Update order status
        order.update_status("Preparing")
        
        # Simulate database operation
        self._save_order_to_database(order)
        
        print(f"Order {order.order_id} is now being prepared.")
        return True
        
    def _save_order_to_database(self, order):
        """
        # Private Method: _save_order_to_database
        # Simulates saving an order to a database
        #
        # Parameters:
        # - order: The Order object to save
        """
        # In a real system, this would interact with a database
        print(f"Database: Order {order.order_id} saved to database")
        
    def mark_order_ready(self, order_id):
        """
        # Method: mark_order_ready
        # Marks an order as ready for pickup/delivery
        #
        # Parameters:
        # - order_id: The ID of the order to mark as ready
        #
        # Returns:
        # - bool: True if marked as ready successfully, False otherwise
        """
        order = self.find_order_by_id(order_id)
        if order:
            if order.status == "Preparing":
                order.update_status("Ready")
                
                # Simulate database operation
                self._update_order_in_database(order)
                
                print(f"Order {order_id} is now ready.")
                return True
            else:
                print(f"Order {order_id} is in {order.status} status and cannot be marked ready.")
                return False
                    
        print(f"Order {order_id} not found.")
        return False
        
    def mark_order_delivered(self, order_id):
        """
        # Method: mark_order_delivered
        # Marks an order as delivered
        #
        # Parameters:
        # - order_id: The ID of the order to mark as delivered
        #
        # Returns:
        # - bool: True if marked as delivered successfully, False otherwise
        """
        order = self.find_order_by_id(order_id)
        if order:
            if order.status == "Ready":
                order.update_status("Delivered")
                
                # Simulate database operation
                self._update_order_in_database(order)
                
                print(f"Order {order_id} has been delivered.")
                return True
            else:
                print(f"Order {order_id} is in {order.status} status and cannot be marked delivered.")
                return False
                    
        print(f"Order {order_id} not found.")
        return False
    
    def _update_order_in_database(self, order):
        """
        # Private Method: _update_order_in_database
        # Simulates updating an order in a database
        #
        # Parameters:
        # - order: The Order object to update
        """
        # In a real system, this would interact with a database
        print(f"Database: Order {order.order_id} updated in database")
        
    def cancel_order(self, order_id):
        """
        # Method: cancel_order
        # Cancels an order and returns items to inventory
        #
        # Parameters:
        # - order_id: The ID of the order to cancel
        #
        # Returns:
        # - bool: True if cancelled successfully, False otherwise
        """
        order = self.find_order_by_id(order_id)
        if not order:
            print(f"Order {order_id} not found.")
            return False
            
        # Only allow cancellation for orders that haven't been delivered
        if order.status == "Delivered":
            print("Cannot cancel an order that has already been delivered.")
            return False
            
        # Return items to inventory
        for item, quantity in order.items.items():
            item.update_quantity(quantity)
            
        # If the order was already processed, subtract from revenue
        if order.status != "Placed" and order.status != "Cart":
            self.revenue -= order.calculate_total_price()
            
        # Update order status
        order.update_status("Cancelled")
        
        # Simulate database operation
        self._update_order_in_database(order)
        
        print(f"Order {order_id} has been cancelled.")
        return True
        
    def get_total_revenue(self):
        """
        # Method: get_total_revenue
        # Gets the total revenue of the restaurant
        #
        # Returns:
        # - float: The total revenue
        """
        return self.revenue
        
    def get_pending_orders(self):
        """
        # Method: get_pending_orders
        # Gets all orders that are not delivered or cancelled
        #
        # Returns:
        # - list: List of pending Order objects
        """
        return [order for order in self.orders if order.status not in ["Delivered", "Cancelled"]]
        
    def get_orders_by_status(self, status):
        """
        # Method: get_orders_by_status
        # Gets all orders with a specific status
        #
        # Parameters:
        # - status: The status to filter by
        #
        # Returns:
        # - list: List of Order objects with the specified status
        """
        return [order for order in self.orders if order.status == status]
        
    def find_order_by_id(self, order_id):
        """
        # Method: find_order_by_id
        # Finds an order by its ID
        #
        # Parameters:
        # - order_id: The ID of the order to find
        #
        # Returns:
        # - Order: The found order or None if not found
        """
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None
        
    def get_daily_revenue(self, date=None):
        """
        # Method: get_daily_revenue
        # Calculates the revenue for a specific date
        #
        # Parameters:
        # - date: The date to calculate revenue for (default: today)
        #
        # Returns:
        # - float: The revenue for the specified date
        """
        if date is None:
            date = datetime.now().date()
        
        # Filter orders by date
        daily_orders = [order for order in self.orders 
                      if order.order_time and order.order_time.date() == date
                      and order.status != "Cancelled"]
        
        # Calculate total revenue for those orders
        return sum(order.calculate_total_price() for order in daily_orders)
        
    def export_daily_report(self, date=None):
        """
        # Method: export_daily_report
        # Exports a daily report to a CSV file
        #
        # Parameters:
        # - date: The date for the report (default: today)
        #
        # Returns:
        # - str: The path to the exported file
        """
        if date is None:
            date = datetime.now().date()
            
        # Format date as string
        date_str = date.strftime('%Y-%m-%d')
        
        # Create the report directory if it doesn't exist
        report_dir = f"{self.data_dir}/reports"
        os.makedirs(report_dir, exist_ok=True)
        
        # Define the report file path
        report_path = f"{report_dir}/daily_report_{date_str}.csv"
        
        # Filter orders for the specified date
        daily_orders = [order for order in self.orders 
                      if order.order_time and order.order_time.date() == date]
        
        try:
            with open(report_path, 'w', newline='') as file:
                writer = csv.writer(file)
                
                # Write header
                writer.writerow(['Order ID', 'Time', 'Status', 'Items', 'Total Price'])
                
                # Write order data
                for order in daily_orders:
                    writer.writerow([
                        order.order_id,
                        order.order_time.strftime('%H:%M:%S'),
                        order.status,
                        order.item_count(),
                        f"${order.calculate_total_price():.2f}"
                    ])
                    
                # Write summary
                writer.writerow([])
                writer.writerow(['Total Orders', len(daily_orders)])
                writer.writerow(['Total Revenue', f"${self.get_daily_revenue(date):.2f}"])
                
            print(f"Daily report exported to {report_path}")
            return report_path
            
        except Exception as e:
            print(f"Error exporting daily report: {e}")
            return None
            
    def add_table(self, table_number, capacity):
        """
        # Method: add_table
        # Adds a table to the restaurant
        #
        # Parameters:
        # - table_number: The table number
        # - capacity: The seating capacity
        #
        # Returns:
        # - bool: True if added successfully, False if table already exists
        """
        # Check if table already exists
        for table in self.tables:
            if table['number'] == table_number:
                print(f"Table {table_number} already exists.")
                return False
                
        # Add the table
        self.tables.append({
            'number': table_number,
            'capacity': capacity,
            'status': 'Available'  # Can be 'Available', 'Occupied', or 'Reserved'
        })
        
        print(f"Table {table_number} added with capacity {capacity}.")
        return True
        
    def set_table_status(self, table_number, status):
        """
        # Method: set_table_status
        # Sets the status of a table
        #
        # Parameters:
        # - table_number: The table number
        # - status: The new status ('Available', 'Occupied', or 'Reserved')
        #
        # Returns:
        # - bool: True if updated successfully, False if table not found
        """
        for table in self.tables:
            if table['number'] == table_number:
                table['status'] = status
                print(f"Table {table_number} is now {status}.")
                return True
                
        print(f"Table {table_number} not found.")
        return False
        
    def find_available_table(self, party_size):
        """
        # Method: find_available_table
        # Finds an available table for a specific party size
        #
        # Parameters:
        # - party_size: The number of people in the party
        #
        # Returns:
        # - dict: The available table or None if no suitable table found
        """
        available_tables = [table for table in self.tables 
                           if table['status'] == 'Available' and table['capacity'] >= party_size]
        
        if not available_tables:
            return None
            
        # Find the smallest table that can accommodate the party
        return min(available_tables, key=lambda t: t['capacity'])
        
    def update_opening_hours(self, day, open_time, close_time):
        """
        # Method: update_opening_hours
        # Updates the opening hours for a specific day
        #
        # Parameters:
        # - day: The day of the week
        # - open_time: The opening time (format: "HH:MM")
        # - close_time: The closing time (format: "HH:MM")
        #
        # Returns:
        # - bool: True if updated successfully, False if day not found
        """
        if day not in self.opening_hours:
            print(f"Invalid day: {day}")
            return False
            
        self.opening_hours[day] = {"open": open_time, "close": close_time}
        print(f"Opening hours for {day} updated: {open_time} - {close_time}")
        return True
        
    def is_open(self, time=None):
        """
        # Method: is_open
        # Checks if the restaurant is open at a specific time
        #
        # Parameters:
        # - time: The time to check (default: current time)
        #
        # Returns:
        # - bool: True if open, False if closed
        """
        if time is None:
            time = datetime.now()
            
        # Get the day of the week
        day = time.strftime('%A')
        
        # Check if the day is in opening_hours
        if day not in self.opening_hours:
            return False
            
        # Get opening and closing times
        opening = datetime.strptime(self.opening_hours[day]["open"], "%H:%M").time()
        closing = datetime.strptime(self.opening_hours[day]["close"], "%H:%M").time()
        
        # Check if current time is within opening hours
        current_time = time.time()
        return opening <= current_time <= closing
        
    def __str__(self):
        """
        # Magic/Dunder Method: __str__
        # Returns a string representation of the restaurant
        # Used when str() is called on an instance
        """
        return f"{self.name} - {self.address} - {self.phone}"