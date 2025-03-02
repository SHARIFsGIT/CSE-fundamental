# -------------------- Restaurant Class --------------------
from menu import Menu

class Restaurant:
    """
    Represents a restaurant with name, employees, and menu.
    """
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()
        self.orders = []
        self.revenue = 0.0
        
    def add_employee(self, employee):
        """Add an employee to the restaurant."""
        # Check if employee with same name already exists
        for emp in self.employees:
            if emp.name == employee.name:
                print(f"Employee {employee.name} already exists.")
                return False
                
        self.employees.append(employee)
        print(f"{employee.name} has joined as {employee.job_title}.")
        return True

    def remove_employee(self, employee_name):
        """Remove an employee from the restaurant by name."""
        for i, employee in enumerate(self.employees):
            if employee.name.lower() == employee_name.lower():
                removed_employee = self.employees.pop(i)
                print(f"{removed_employee.name} has been removed from the employee list.")
                return True
        print(f"No employee named {employee_name} was found.")
        return False

    def find_employee(self, employee_name):
        """Find an employee by name."""
        for employee in self.employees:
            if employee.name.lower() == employee_name.lower():
                return employee
        return None

    def show_all_employees(self):
        """Display all employees with their details."""
        if not self.employees:
            print("No employees currently hired.")
            return

        print("\n" + "="*70)
        print(f"{'Name':<20}{'Job Title':<20}{'Salary':^10}{'Contact':<20}")
        print("-"*70)
        for emp in self.employees:
            print(f"{emp.name:<20}{emp.job_title:<20}${emp.salary:<9.2f}{emp.phone:<20}")
        print("="*70 + "\n")
        
    def add_food_item(self, food_item):
        """Add a food item to the restaurant's menu."""
        return self.menu.add_item(food_item)
        
    def remove_food_item(self, item_name):
        """Remove a food item from the restaurant's menu."""
        return self.menu.remove_item(item_name)
        
    def find_food_item(self, item_name):
        """Find a food item by name."""
        return self.menu.find_item(item_name)
        
    def display_menu(self):
        """Display the restaurant's menu."""
        print(f"\n{self.name}'s Menu")
        self.menu.display_menu()
        
    def process_order(self, order):
        """Process a placed order."""
        if order.status != "Placed":
            print("This order has not been placed yet.")
            return False
            
        # Add order to restaurant's orders
        self.orders.append(order)
        
        # Update revenue
        self.revenue += order.calculate_total_price()
        
        # Update order status
        order.status = "Preparing"
        
        print(f"Order {order.order_id} is now being prepared.")
        return True
        
    def mark_order_ready(self, order_id):
        """Mark an order as ready for pickup/delivery."""
        for order in self.orders:
            if order.order_id == order_id:
                if order.status == "Preparing":
                    order.status = "Ready"
                    print(f"Order {order_id} is now ready.")
                    return True
                else:
                    print(f"Order {order_id} is in {order.status} status and cannot be marked ready.")
                    return False
                    
        print(f"Order {order_id} not found.")
        return False
        
    def mark_order_delivered(self, order_id):
        """Mark an order as delivered."""
        for order in self.orders:
            if order.order_id == order_id:
                if order.status == "Ready":
                    order.status = "Delivered"
                    print(f"Order {order_id} has been delivered.")
                    return True
                else:
                    print(f"Order {order_id} is in {order.status} status and cannot be marked delivered.")
                    return False
                    
        print(f"Order {order_id} not found.")
        return False
        
    def get_total_revenue(self):
        """Get the total revenue of the restaurant."""
        return self.revenue
        
    def get_pending_orders(self):
        """Get all orders that are not delivered."""
        return [order for order in self.orders if order.status != "Delivered"]
        
    def get_orders_by_status(self, status):
        """Get all orders with a specific status."""
        return [order for order in self.orders if order.status == status]
        
    def find_order_by_id(self, order_id):
        """Find an order by its ID."""
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None