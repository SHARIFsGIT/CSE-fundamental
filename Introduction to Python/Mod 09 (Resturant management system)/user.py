# -------------------- User Classes --------------------
"""
This module defines the User classes for the restaurant management system.
It includes the base User class and derived classes for Admin, Employee, and Customer.
"""
from abc import ABC, abstractmethod
from order import Order
from datetime import datetime, timedelta

class User(ABC):
    """
    # Class: User (Abstract Base Class)
    # Purpose: Base class for all users in the system
    # Note: ABC means this is an Abstract Base Class that cannot be instantiated directly
    #
    # Properties:
    # - name: User's name
    # - phone: User's phone number
    # - email: User's email address
    # - address: User's physical address
    # - user_id: Unique identifier for the user (new)
    # - created_at: When the user account was created (new)
    """
    def __init__(self, name, phone, email, address):
        """
        # Constructor
        # Initializes a new instance of the User class
        #
        # Parameters:
        # - name: User's name
        # - phone: User's phone number
        # - email: User's email address
        # - address: User's physical address
        """
        # Instance attributes/properties
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.user_id = self._generate_user_id()
        self.created_at = datetime.now()
        self.last_login = datetime.now()
        
    def _generate_user_id(self):
        """
        # Private Method: _generate_user_id
        # Generates a unique user ID
        #
        # Returns:
        # - str: A unique ID
        """
        # In a real system, this would generate a truly unique ID
        # For this example, we'll use a timestamp + name-based ID
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        name_part = ''.join(c for c in self.name if c.isalnum())[:5].upper()
        return f"USER-{name_part}-{timestamp}"
        
    def update_contact_info(self, phone=None, email=None, address=None):
        """
        # Method: update_contact_info
        # Updates the user's contact information
        #
        # Parameters:
        # - phone: New phone number (optional)
        # - email: New email address (optional)
        # - address: New physical address (optional)
        #
        # Returns:
        # - bool: True to indicate successful update
        """
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address
        return True
        
    def display_info(self):
        """
        # Method: display_info
        # Displays the user's information
        """
        print(f"\nUser Information:")
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")
        print(f"Account Created: {self.created_at}")
        
    def record_login(self):
        """
        # Method: record_login
        # Records a user login by updating the last_login timestamp
        """
        self.last_login = datetime.now()
        
    @abstractmethod
    def get_role(self):
        """
        # Abstract Method: get_role
        # Returns the user's role
        # Must be implemented by derived classes
        """
        pass


# -------------------- Admin Class --------------------

class Admin(User):
    """
    # Class: Admin (inherits from User)
    # Purpose: Represents an admin user who can manage employees and menu items
    #
    # Properties:
    # - Inherits all properties from User
    # - role: The user's role (always "Admin")
    # - admin_level: The admin's access level (new)
    """
    def __init__(self, name, phone, email, address, admin_level="Full"):
        """
        # Constructor
        # Initializes a new instance of the Admin class
        #
        # Parameters:
        # - name: Admin's name
        # - phone: Admin's phone number
        # - email: Admin's email address
        # - address: Admin's physical address
        # - admin_level: Admin's access level (default: "Full")
        """
        # Call the parent class constructor
        super().__init__(name, phone, email, address)
        self.role = "Admin"
        self.admin_level = admin_level  # Can be "Full", "Menu", "Staff", etc.

    def get_role(self):
        """
        # Method: get_role
        # Returns the user's role
        #
        # Returns:
        # - str: The role ("Admin")
        """
        return self.role

    def add_employee(self, restaurant, employee):
        """
        # Method: add_employee
        # Adds an employee to the restaurant
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - employee: The Employee object to add
        #
        # Returns:
        # - bool: True if added successfully, False otherwise
        """
        return restaurant.add_employee(employee)

    def remove_employee(self, restaurant, employee_name):
        """
        # Method: remove_employee
        # Removes an employee from the restaurant
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - employee_name: The name of the employee to remove
        #
        # Returns:
        # - bool: True if removed successfully, False otherwise
        """
        return restaurant.remove_employee(employee_name)

    def display_all_employees(self, restaurant):
        """
        # Method: display_all_employees
        # Displays all employees in the restaurant
        #
        # Parameters:
        # - restaurant: The Restaurant object
        """
        restaurant.show_all_employees()

    def add_menu_item(self, restaurant, menu_item):
        """
        # Method: add_menu_item
        # Adds a food item to the restaurant's menu
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - menu_item: The FoodItem object to add
        #
        # Returns:
        # - bool: True if added successfully, False otherwise
        """
        return restaurant.add_food_item(menu_item)

    def remove_menu_item(self, restaurant, item_name):
        """
        # Method: remove_menu_item
        # Removes a food item from the restaurant's menu
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - item_name: The name of the item to remove
        #
        # Returns:
        # - bool: True if removed successfully, False otherwise
        """
        return restaurant.remove_food_item(item_name)
        
    def update_menu_item(self, restaurant, item_name, new_price=None, new_quantity=None):
        """
        # Method: update_menu_item
        # Updates a food item in the restaurant's menu
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - item_name: The name of the item to update
        # - new_price: The new price (optional)
        # - new_quantity: The new quantity (optional)
        #
        # Returns:
        # - bool: True if updated successfully, False otherwise
        """
        return restaurant.menu.update_item(item_name, new_price, new_quantity)
        
    def view_revenue(self, restaurant):
        """
        # Method: view_revenue
        # Views the restaurant's total revenue
        #
        # Parameters:
        # - restaurant: The Restaurant object
        #
        # Returns:
        # - float: The total revenue
        """
        revenue = restaurant.get_total_revenue()
        print(f"Total Revenue: ${revenue:.2f}")
        return revenue
        
    def generate_revenue_report(self, restaurant, start_date=None, end_date=None):
        """
        # Method: generate_revenue_report
        # Generates a revenue report for a specific date range
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - start_date: The start date for the report (optional)
        # - end_date: The end date for the report (optional)
        """
        if start_date is None:
            start_date = datetime.now().date()
        if end_date is None:
            end_date = start_date
            
        print("\n" + "="*60)
        print(f"Revenue Report: {start_date} to {end_date}")
        print("-"*60)
        
        total_revenue = 0
        total_orders = 0
        
        current_date = start_date
        while current_date <= end_date:
            # Get daily revenue
            daily_revenue = restaurant.get_daily_revenue(current_date)
            
            # Count orders for the day
            daily_orders = [order for order in restaurant.orders 
                          if order.order_time and order.order_time.date() == current_date
                          and order.status != "Cancelled"]
            
            # Add to totals
            total_revenue += daily_revenue
            total_orders += len(daily_orders)
            
            # Display daily data
            print(f"{current_date}: ${daily_revenue:.2f} ({len(daily_orders)} orders)")
            
            # Move to next day
            current_date = current_date + timedelta(days=1)
            
        print("-"*60)
        print(f"Total Orders: {total_orders}")
        print(f"Total Revenue: ${total_revenue:.2f}")
        print("="*60 + "\n")
        
        return total_revenue

    def display_info(self):
        """
        # Method: display_info
        # Displays the admin's information
        # Overrides the parent class method
        """
        super().display_info()  # Call the parent class method
        print(f"Role: {self.role}")
        print(f"Admin Level: {self.admin_level}\n")


# -------------------- Employee Class --------------------

class Employee(User):
    """
    # Class: Employee (inherits from User)
    # Purpose: Represents an employee of the restaurant
    #
    # Properties:
    # - Inherits all properties from User
    # - age: Employee's age
    # - job_title: Employee's job title
    # - salary: Employee's salary
    # - hire_date: When the employee was hired (new)
    # - employee_id: Unique employee identifier (new)
    """
    def __init__(self, name, phone, email, address, age, job_title, salary):
        """
        # Constructor
        # Initializes a new instance of the Employee class
        #
        # Parameters:
        # - name: Employee's name
        # - phone: Employee's phone number
        # - email: Employee's email address
        # - address: Employee's physical address
        # - age: Employee's age
        # - job_title: Employee's job title
        # - salary: Employee's salary
        """
        # Call the parent class constructor
        super().__init__(name, phone, email, address)
        self.age = age
        self.job_title = job_title
        self.salary = salary
        self.hire_date = datetime.now()
        self.employee_id = self._generate_employee_id()
        self.shifts = []  # Store the employee's work shifts
        
    def _generate_employee_id(self):
        """
        # Private Method: _generate_employee_id
        # Generates a unique employee ID
        #
        # Returns:
        # - str: A unique employee ID
        """
        # In a real system, this would generate a truly unique ID
        timestamp = datetime.now().strftime("%y%m")
        name_part = ''.join(c for c in self.name if c.isalnum())[:3].upper()
        return f"EMP-{name_part}-{timestamp}"
        
    def get_role(self):
        """
        # Method: get_role
        # Returns the user's role
        #
        # Returns:
        # - str: The role (job title)
        """
        return self.job_title
        
    def display_info(self):
        """
        # Method: display_info
        # Displays the employee's information
        # Overrides the parent class method
        """
        super().display_info()  # Call the parent class method
        print(f"Employee ID: {self.employee_id}")
        print(f"Age: {self.age}")
        print(f"Job Title: {self.job_title}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Hire Date: {self.hire_date}")
        print("\n")
    
    def add_shift(self, day, start_time, end_time):
        """
        # Method: add_shift
        # Adds a work shift for the employee
        #
        # Parameters:
        # - day: The day of the week
        # - start_time: The shift start time
        # - end_time: The shift end time
        #
        # Returns:
        # - bool: True to indicate successful addition
        """
        self.shifts.append({
            'day': day,
            'start': start_time,
            'end': end_time
        })
        return True
    
    def get_shifts(self):
        """
        # Method: get_shifts
        # Returns the employee's work shifts
        #
        # Returns:
        # - list: The employee's shifts
        """
        return self.shifts
        
    def update_salary(self, new_salary):
        """
        # Method: update_salary
        # Updates the employee's salary
        #
        # Parameters:
        # - new_salary: The new salary amount
        #
        # Returns:
        # - bool: True to indicate successful update
        """
        if new_salary <= 0:
            print("Salary must be positive.")
            return False
            
        self.salary = new_salary
        print(f"{self.name}'s salary updated to ${new_salary:.2f}")
        return True
        
    def process_customer_order(self, restaurant, order):
        """
        # Method: process_customer_order
        # Processes a customer's order
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - order: The Order object to process
        #
        # Returns:
        # - bool: True if processed successfully, False otherwise
        """
        return restaurant.process_order(order)
        
    def mark_order_ready(self, restaurant, order_id):
        """
        # Method: mark_order_ready
        # Marks an order as ready for pickup/delivery
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - order_id: The ID of the order to mark as ready
        #
        # Returns:
        # - bool: True if marked as ready successfully, False otherwise
        """
        return restaurant.mark_order_ready(order_id)
        
    def mark_order_delivered(self, restaurant, order_id):
        """
        # Method: mark_order_delivered
        # Marks an order as delivered
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - order_id: The ID of the order to mark as delivered
        #
        # Returns:
        # - bool: True if marked as delivered successfully, False otherwise
        """
        return restaurant.mark_order_delivered(order_id)
    
    def view_pending_orders(self, restaurant):
        """
        # Method: view_pending_orders
        # Displays all pending orders (not delivered or cancelled)
        #
        # Parameters:
        # - restaurant: The Restaurant object
        """
        pending_orders = restaurant.get_pending_orders()
        
        if not pending_orders:
            print("No pending orders.")
            return
            
        print("\n" + "="*70)
        print("Pending Orders")
        print("-"*70)
        print(f"{'Order ID':<25}{'Status':<12}{'Items':<8}{'Total':<10}{'Time':<20}")
        print("-"*70)
        
        for order in pending_orders:
            print(f"{order.order_id:<25}{order.status:<12}{order.item_count():<8}${order.calculate_total_price():<9.2f}{str(order.order_time)[:19]:<20}")
            
        print("="*70 + "\n")
        
        return pending_orders


# -------------------- Customer Class --------------------

class Customer(User):
    """
    # Class: Customer (inherits from User)
    # Purpose: Represents a customer who can place orders
    #
    # Properties:
    # - Inherits all properties from User
    # - cart: The customer's current shopping cart (Order object)
    # - order_history: List of previous orders
    # - loyalty_points: Customer's loyalty program points (new)
    # - payment_methods: List of the customer's payment methods (new)
    # - preferences: Dictionary of customer preferences (new)
    """
    def __init__(self, name, phone, email, address):
        """
        # Constructor
        # Initializes a new instance of the Customer class
        #
        # Parameters:
        # - name: Customer's name
        # - phone: Customer's phone number
        # - email: Customer's email address
        # - address: Customer's physical address
        """
        # Call the parent class constructor
        super().__init__(name, phone, email, address)
        self.cart = Order()
        self.order_history = []
        self.loyalty_points = 0
        self.payment_methods = []
        self.preferences = {
            'favorite_items': [],
            'dietary_restrictions': [],
            'allergies': [],
            'preferred_payment': None
        }
        
    def get_role(self):
        """
        # Method: get_role
        # Returns the user's role
        #
        # Returns:
        # - str: The role ("Customer")
        """
        return "Customer"

    def view_menu(self, restaurant):
        """
        # Method: view_menu
        # Views the restaurant's menu
        #
        # Parameters:
        # - restaurant: The Restaurant object
        """
        restaurant.display_menu()
        
    def view_category(self, restaurant, category):
        """
        # Method: view_category
        # Views items in a specific menu category
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - category: The category to view
        """
        restaurant.menu.display_category(category)

    def add_item_to_cart(self, restaurant, item_name, quantity):
        """
        # Method: add_item_to_cart
        # Adds a food item to the customer's cart
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - item_name: The name of the item to add
        # - quantity: The quantity to add
        #
        # Returns:
        # - bool: True if added successfully, False otherwise
        """
        menu_item = restaurant.find_food_item(item_name)
        if not menu_item:
            print(f"Sorry, {item_name} is not available in the menu.")
            return False
            
        if quantity > menu_item.quantity:
            print(f"Sorry, we only have {menu_item.quantity} of {item_name} left.")
            return False
            
        self.cart.add_item(menu_item, quantity)
        print(f"{menu_item.name} (x{quantity}) added to your cart.")
        return True

    def view_cart(self):
        """
        # Method: view_cart
        # Views the customer's current cart
        """
        if self.cart.is_empty():
            print("Your cart is empty.")
            return
            
        print("\n" + "="*70)
        print("Your Cart")
        print("-"*70)
        print(f"{'Item Name':<30}{'Price':^10}{'Quantity':^10}{'Subtotal':>10}")
        print("-"*70)
        
        for item, quantity in self.cart.items.items():
            # Use discounted price if applicable
            item_price = item.get_discounted_price()
            subtotal = item_price * quantity
            
            # Show original price if discounted
            if item.discount_percentage > 0:
                price_display = f"${item_price:.2f} (${item.price:.2f})"
            else:
                price_display = f"${item_price:.2f}"
                
            print(f"{item.name:<30}{price_display:<15}{quantity:^5}${subtotal:>9.2f}")
            
        print("-"*70)
        
        # Calculate and display subtotal, tax, and total
        subtotal = self.cart.calculate_subtotal()
        tax = self.cart.calculate_tax()
        total = self.cart.calculate_grand_total()
        
        print(f"{'Subtotal:':<50}${subtotal:>9.2f}")
        print(f"{'Tax (5%):':<50}${tax:>9.2f}")
        print(f"{'Total Amount:':<50}${total:>9.2f}")
        print("="*70 + "\n")

    def remove_item_from_cart(self, restaurant, item_name):
        """
        # Method: remove_item_from_cart
        # Removes a food item from the customer's cart
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - item_name: The name of the item to remove
        #
        # Returns:
        # - bool: True if removed successfully, False otherwise
        """
        menu_item = restaurant.find_food_item(item_name)
        if not menu_item:
            print(f"Sorry, {item_name} is not available in the menu.")
            return False
            
        if menu_item not in self.cart.items:
            print(f"Sorry, {item_name} is not in your cart.")
            return False
            
        quantity = self.cart.items[menu_item]
        self.cart.remove_item(menu_item)
        print(f"{menu_item.name} (x{quantity}) removed from your cart.")
        return True
        
    def update_cart_item_quantity(self, restaurant, item_name, new_quantity):
        """
        # Method: update_cart_item_quantity
        # Updates the quantity of a food item in the customer's cart
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - item_name: The name of the item to update
        # - new_quantity: The new quantity
        #
        # Returns:
        # - bool: True if updated successfully, False otherwise
        """
        menu_item = restaurant.find_food_item(item_name)
        if not menu_item:
            print(f"Sorry, {item_name} is not available in the menu.")
            return False
            
        if menu_item not in self.cart.items:
            print(f"Sorry, {item_name} is not in your cart.")
            return False
            
        if new_quantity <= 0:
            return self.remove_item_from_cart(restaurant, item_name)
            
        # Check if the requested quantity is available
        current_quantity = self.cart.items[menu_item]
        additional_quantity = new_quantity - current_quantity
        
        if additional_quantity > 0 and not menu_item.is_available(additional_quantity):
            print(f"Sorry, only {menu_item.quantity} of {item_name} available.")
            return False
            
        self.cart.update_item_quantity(menu_item, new_quantity)
        print(f"{menu_item.name} quantity updated to {new_quantity}.")
        return True
    
    def add_special_instructions(self, instructions):
        """
        # Method: add_special_instructions
        # Adds special instructions to the current order
        #
        # Parameters:
        # - instructions: The special instructions
        """
        self.cart.add_special_instructions(instructions)
        print("Special instructions added.")
    
    def place_order(self, payment_method=None, delivery_address=None, table_number=None):
        """
        # Method: place_order
        # Places the customer's order
        #
        # Parameters:
        # - payment_method: The payment method (optional)
        # - delivery_address: The delivery address (optional, uses default if None)
        # - table_number: The table number (for dine-in orders, optional)
        #
        # Returns:
        # - Order: The placed order or None if unsuccessful
        """
        if self.cart.is_empty():
            print("Cannot place an empty order.")
            return None
            
        # Set payment method
        if payment_method:
            self.cart.set_payment_method(payment_method)
        elif self.preferences['preferred_payment']:
            self.cart.set_payment_method(self.preferences['preferred_payment'])
        else:
            # Default to cash
            self.cart.set_payment_method("Cash")
            
        # Use provided delivery address or default address
        use_address = delivery_address or self.address
        
        # Place the order
        if self.cart.place_order(customer_id=self.user_id, 
                                delivery_address=use_address,
                                table_number=table_number):
            # Create a new order object for the next order
            order_placed = self.cart
            self.order_history.append(order_placed)
            self.cart = Order()
            
            # Add loyalty points (1 point per dollar)
            points_earned = int(order_placed.calculate_total_price())
            self.add_loyalty_points(points_earned)
            
            print(f"Order {order_placed.order_id} has been placed successfully!")
            print(f"You earned {points_earned} loyalty points!")
            return order_placed
        
        return None
            
    def view_order_history(self):
        """
        # Method: view_order_history
        # Views the customer's order history
        """
        if not self.order_history:
            print("You have no previous orders.")
            return
            
        print("\n" + "="*70)
        print("Your Order History")
        print("-"*70)
        
        for order in self.order_history:
            total = order.calculate_total_price()
            print(f"Order ID: {order.order_id}")
            print(f"Date: {order.order_time}")
            print(f"Status: {order.status}")
            print(f"Items: {order.item_count()}")
            print(f"Total: ${total:.2f}")
            
            # Show order details if it has items
            if order.items:
                print("\nItems:")
                for item, quantity in order.items.items():
                    print(f"  - {item.name} (x{quantity}): ${item.price * quantity:.2f}")
                    
            print("-"*70)
            
        print("="*70 + "\n")
        
    def add_loyalty_points(self, points):
        """
        # Method: add_loyalty_points
        # Adds loyalty points to the customer's account
        #
        # Parameters:
        # - points: The number of points to add
        #
        # Returns:
        # - int: The new total points
        """
        self.loyalty_points += points
        return self.loyalty_points
        
    def use_loyalty_points(self, points):
        """
        # Method: use_loyalty_points
        # Uses loyalty points from the customer's account
        #
        # Parameters:
        # - points: The number of points to use
        #
        # Returns:
        # - bool: True if successful, False if not enough points
        """
        if points > self.loyalty_points:
            print(f"Not enough loyalty points. You have {self.loyalty_points} points.")
            return False
            
        self.loyalty_points -= points
        print(f"Used {points} loyalty points. Remaining: {self.loyalty_points} points.")
        return True
        
    def add_payment_method(self, method_type, details):
        """
        # Method: add_payment_method
        # Adds a payment method to the customer's account
        #
        # Parameters:
        # - method_type: The type of payment method (e.g., "Credit Card", "PayPal")
        # - details: The payment method details
        #
        # Returns:
        # - bool: True to indicate successful addition
        """
        self.payment_methods.append({
            'type': method_type,
            'details': details,
            'added_on': datetime.now()
        })
        print(f"{method_type} added as a payment method.")
        return True
        
    def set_preferred_payment(self, method_type):
        """
        # Method: set_preferred_payment
        # Sets the preferred payment method
        #
        # Parameters:
        # - method_type: The type of payment method
        #
        # Returns:
        # - bool: True if successful, False if method not found
        """
        # Check if the payment method exists
        for method in self.payment_methods:
            if method['type'] == method_type:
                self.preferences['preferred_payment'] = method_type
                print(f"{method_type} set as preferred payment method.")
                return True
                
        print(f"Payment method {method_type} not found.")
        return False
        
    def add_to_favorites(self, restaurant, item_name):
        """
        # Method: add_to_favorites
        # Adds a menu item to the customer's favorites
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - item_name: The name of the item to add
        #
        # Returns:
        # - bool: True if added successfully, False otherwise
        """
        menu_item = restaurant.find_food_item(item_name)
        if not menu_item:
            print(f"Sorry, {item_name} is not available in the menu.")
            return False
            
        if item_name in self.preferences['favorite_items']:
            print(f"{item_name} is already in your favorites.")
            return False
            
        self.preferences['favorite_items'].append(item_name)
        print(f"{item_name} added to your favorites.")
        return True
        
    def add_dietary_restriction(self, restriction):
        """
        # Method: add_dietary_restriction
        # Adds a dietary restriction to the customer's preferences
        #
        # Parameters:
        # - restriction: The dietary restriction
        #
        # Returns:
        # - bool: True to indicate successful addition
        """
        if restriction in self.preferences['dietary_restrictions']:
            print(f"{restriction} is already in your dietary restrictions.")
            return False
            
        self.preferences['dietary_restrictions'].append(restriction)
        print(f"{restriction} added to your dietary restrictions.")
        return True
        
    def add_allergy(self, allergy):
        """
        # Method: add_allergy
        # Adds an allergy to the customer's preferences
        #
        # Parameters:
        # - allergy: The allergy
        #
        # Returns:
        # - bool: True to indicate successful addition
        """
        if allergy in self.preferences['allergies']:
            print(f"{allergy} is already in your allergies.")
            return False
            
        self.preferences['allergies'].append(allergy)
        print(f"{allergy} added to your allergies.")
        return True
        
    def display_info(self):
        """
        # Method: display_info
        # Displays the customer's information
        # Overrides the parent class method
        """
        super().display_info()  # Call the parent class method
        print(f"Role: Customer")
        print(f"Loyalty Points: {self.loyalty_points}")
        
        # Display preferences
        print("\nPreferences:")
        print(f"Favorite Items: {', '.join(self.preferences['favorite_items']) or 'None'}")
        print(f"Dietary Restrictions: {', '.join(self.preferences['dietary_restrictions']) or 'None'}")
        print(f"Allergies: {', '.join(self.preferences['allergies']) or 'None'}")
        print(f"Preferred Payment: {self.preferences['preferred_payment'] or 'None'}")
        
        # Display payment methods
        print("\nPayment Methods:")
        if not self.payment_methods:
            print("None")
        else:
            for method in self.payment_methods:
                print(f"- {method['type']}")
                
        print("\n")
    
    def search_menu(self, restaurant, keyword):
        """
        # Method: search_menu
        # Searches the restaurant's menu for items matching a keyword
        #
        # Parameters:
        # - restaurant: The Restaurant object
        # - keyword: The search keyword
        """
        results = restaurant.menu.search_items(keyword)
        
        if not results:
            print(f"No items found matching '{keyword}'.")
            return
            
        print("\n" + "="*70)
        print(f"Search Results for '{keyword}'")
        print("-"*70)
        print(f"{'Item Name':<30}{'Price':^10}{'Category':<15}{'Stock':^10}")
        print("-"*70)
        
        for item in results:
            print(f"{item.name:<30}${item.price:<9.2f}{item.category:<15}{item.quantity:^10}")
            
        print("="*70 + "\n")
        
        return results