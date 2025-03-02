# -------------------- User Classes --------------------
from abc import ABC, abstractmethod
from order import Order

class User(ABC):
    """
    Abstract base class for all users in the system.
    """
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
    def update_contact_info(self, phone=None, email=None, address=None):
        """Update the user's contact information."""
        if phone:
            self.phone = phone
        if email:
            self.email = email
        if address:
            self.address = address
        return True


# -------------------- Admin Class --------------------

class Admin(User):
    """
    Represents an admin user who can manage employees and menu items.
    """
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.role = "Admin"

    def add_employee(self, restaurant, employee):
        """Add an employee to the restaurant."""
        return restaurant.add_employee(employee)

    def remove_employee(self, restaurant, employee_name):
        """Remove an employee from the restaurant."""
        return restaurant.remove_employee(employee_name)

    def display_all_employees(self, restaurant):
        """Display all employees in the restaurant."""
        restaurant.show_all_employees()

    def add_menu_item(self, restaurant, menu_item):
        """Add a food item to the restaurant's menu."""
        return restaurant.add_food_item(menu_item)

    def remove_menu_item(self, restaurant, item_name):
        """Remove a food item from the restaurant's menu."""
        return restaurant.remove_food_item(item_name)
        
    def update_menu_item(self, restaurant, item_name, new_price=None, new_quantity=None):
        """Update a food item in the restaurant's menu."""
        return restaurant.menu.update_item(item_name, new_price, new_quantity)
        
    def view_revenue(self, restaurant):
        """View the restaurant's total revenue."""
        revenue = restaurant.get_total_revenue()
        print(f"Total Revenue: ${revenue:.2f}")
        return revenue


# -------------------- Employee Class --------------------

class Employee(User):
    """
    Represents an employee of the restaurant.
    """
    def __init__(self, name, phone, email, address, age, job_title, salary):
        super().__init__(name, phone, email, address)
        self.age = age
        self.job_title = job_title
        self.salary = salary
        
    def display_info(self):
        """Display the employee's information."""
        print(f"\nEmployee Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Job Title: {self.job_title}")
        print(f"Salary: ${self.salary:.2f}")
        print(f"Contact: {self.phone}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}\n")
        
    def process_customer_order(self, restaurant, order):
        """Process a customer's order."""
        return restaurant.process_order(order)
        
    def mark_order_ready(self, restaurant, order_id):
        """Mark an order as ready for pickup/delivery."""
        return restaurant.mark_order_ready(order_id)
        
    def mark_order_delivered(self, restaurant, order_id):
        """Mark an order as delivered."""
        return restaurant.mark_order_delivered(order_id)


# -------------------- Customer Class --------------------

class Customer(User):
    """
    Represents a customer who can place orders.
    """
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()
        self.order_history = []

    def view_menu(self, restaurant):
        """View the restaurant's menu."""
        restaurant.display_menu()

    def add_item_to_cart(self, restaurant, item_name, quantity):
        """Add a food item to the customer's cart."""
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
        """View the customer's current cart."""
        if self.cart.is_empty():
            print("Your cart is empty.")
            return
            
        print("\n" + "="*60)
        print("Your Cart")
        print("-"*60)
        print(f"{'Item Name':<30}{'Price':^10}{'Quantity':^10}{'Subtotal':>10}")
        print("-"*60)
        
        for item, quantity in self.cart.items.items():
            subtotal = item.price * quantity
            print(f"{item.name:<30}${item.price:^9.2f}{quantity:^10}${subtotal:>9.2f}")
            
        print("-"*60)
        print(f"{'Total Amount:':<50}${self.cart.calculate_total_price():>9.2f}")
        print("="*60 + "\n")

    def remove_item_from_cart(self, restaurant, item_name):
        """Remove a food item from the customer's cart."""
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
        """Update the quantity of a food item in the customer's cart."""
        menu_item = restaurant.find_food_item(item_name)
        if not menu_item:
            print(f"Sorry, {item_name} is not available in the menu.")
            return False
            
        if menu_item not in self.cart.items:
            print(f"Sorry, {item_name} is not in your cart.")
            return False
            
        if new_quantity <= 0:
            return self.remove_item_from_cart(restaurant, item_name)
            
        self.cart.update_item_quantity(menu_item, new_quantity)
        print(f"{menu_item.name} quantity updated to {new_quantity}.")
        return True
    
    def place_order(self):
        """Place the customer's order."""
        if self.cart.is_empty():
            print("Cannot place an empty order.")
            return None
            
        if self.cart.place_order():
            # Create a new order object for the next order
            order_placed = self.cart
            self.order_history.append(order_placed)
            self.cart = Order()
            
            print(f"Order {order_placed.order_id} has been placed successfully!")
            return order_placed
        
        return None
            
    def view_order_history(self):
        """View the customer's order history."""
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
            print("-"*70)
            
        print("="*70 + "\n")