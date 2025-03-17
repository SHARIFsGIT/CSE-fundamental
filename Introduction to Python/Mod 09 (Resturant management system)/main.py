"""
Restaurant Management System
A comprehensive system for managing restaurant operations including menu management,
employee management, order processing, and customer service.

This file contains the main entry point and UI controllers for the application.
"""

# -------------------- Main Application --------------------
from food_item import FoodItem
from restaurent import Restaurant
from user import Admin, Customer, Employee
from datetime import datetime
import os
import time
import random


def clear_console():
    """
    # Function: clear_console
    # Clears the console screen for better UI
    """
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')


def init_data_directory():
    """
    # Function: init_data_directory
    # Creates the necessary data directories for the restaurant system
    """
    # Create data directory structure
    os.makedirs("data", exist_ok=True)
    os.makedirs("data/orders", exist_ok=True)
    os.makedirs("data/reports", exist_ok=True)
    os.makedirs("data/logs", exist_ok=True)
    # The `exist_ok=True` parameter ensures that no error occurs if the directory already exists



def initialize_menu(restaurant):
    """
    # Function: initialize_menu
    # Adds sample food items to the restaurant's menu
    #
    # Parameters:
    # - restaurant: The Restaurant object
    """
    # Add Appetizers
    restaurant.add_food_item(FoodItem(
        name="Vegetable Spring Rolls", 
        price=12.99, 
        quantity=100,
        category="Appetizers",
        description="Crispy spring rolls filled with fresh vegetables",
        ingredients=["Cabbage", "Carrot", "Bean sprouts", "Spring roll wrappers"]
    ))
    restaurant.add_food_item(FoodItem(
        name="Chicken Wings", 
        price=16.99, 
        quantity=80,
        category="Appetizers",
        description="Spicy chicken wings with blue cheese dip",
        ingredients=["Chicken wings", "Hot sauce", "Butter", "Garlic"]
    ))
    
    # Add Main Courses
    restaurant.add_food_item(FoodItem(
        name="Biriyani", 
        price=25.99, 
        quantity=50,
        category="Main Course",
        description="Aromatic rice dish with meat and spices",
        ingredients=["Basmati rice", "Chicken/Mutton", "Onions", "Spices"]
    ))
    restaurant.add_food_item(FoodItem(
        name="Beef Curry", 
        price=35.00, 
        quantity=30,
        category="Main Course",
        description="Slow-cooked beef curry with aromatic spices",
        ingredients=["Beef", "Onions", "Tomatoes", "Spices"]
    ))
    restaurant.add_food_item(FoodItem(
        name="Grilled Salmon", 
        price=32.99, 
        quantity=25,
        category="Main Course",
        description="Fresh salmon fillet grilled to perfection",
        ingredients=["Salmon", "Lemon", "Herbs", "Olive oil"]
    ))
    
    # Add Sides
    restaurant.add_food_item(FoodItem(
        name="Paratha", 
        price=3.00, 
        quantity=100,
        category="Sides",
        description="Flaky flatbread",
        ingredients=["Flour", "Oil", "Salt"]
    ))
    restaurant.add_food_item(FoodItem(
        name="Mashed Potatoes", 
        price=8.99, 
        quantity=60,
        category="Sides",
        description="Creamy garlic mashed potatoes",
        ingredients=["Potatoes", "Butter", "Milk", "Garlic"]
    ))
    
    # Add Desserts
    restaurant.add_food_item(FoodItem(
        name="Chocolate Cake", 
        price=14.99, 
        quantity=40,
        category="Desserts",
        description="Rich chocolate cake with ganache",
        ingredients=["Flour", "Sugar", "Cocoa powder", "Eggs"]
    ))
    restaurant.add_food_item(FoodItem(
        name="Cheesecake", 
        price=15.99, 
        quantity=35,
        category="Desserts",
        description="Creamy cheesecake with fruit topping",
        ingredients=["Cream cheese", "Sugar", "Eggs", "Berries"]
    ))
    
    # Add Beverages
    restaurant.add_food_item(FoodItem(
        name="Borhani", 
        price=4.00, 
        quantity=60,
        category="Beverages",
        description="Traditional yogurt-based drink",
        ingredients=["Yogurt", "Mint", "Spices"]
    ))
    restaurant.add_food_item(FoodItem(
        name="Fresh Juice", 
        price=6.99, 
        quantity=70,
        category="Beverages",
        description="Freshly squeezed seasonal fruit juice",
        ingredients=["Seasonal fruits"]
    ))
    restaurant.add_food_item(FoodItem(
        name="Soft Drinks", 
        price=3.99, 
        quantity=200,
        category="Beverages",
        description="Various carbonated soft drinks",
        ingredients=["Carbonated water", "Sugar", "Flavors"]
    ))
    
    # Add Snacks
    restaurant.add_food_item(FoodItem(
        name="Shingara", 
        price=1.99, 
        quantity=200,
        category="Snacks",
        description="Triangular pastry filled with spiced potatoes",
        ingredients=["Flour", "Potatoes", "Peas", "Spices"]
    ))


def initialize_tables(restaurant):
    """
    # Function: initialize_tables
    # Adds sample tables to the restaurant
    #
    # Parameters:
    # - restaurant: The Restaurant object
    """
    # Add tables with different capacities
    restaurant.add_table(1, 2)  # Table #1 with 2 seats
    restaurant.add_table(2, 2)  # Table #2 with 2 seats
    restaurant.add_table(3, 4)  # Table #3 with 4 seats
    restaurant.add_table(4, 4)  # Table #4 with 4 seats
    restaurant.add_table(5, 6)  # Table #5 with 6 seats
    restaurant.add_table(6, 8)  # Table #6 with 8 seats


def admin_menu(restaurant, admin):
    """
    # Function: admin_menu
    # Provides the admin interface for managing the restaurant
    #
    # Parameters:
    # - restaurant: The Restaurant object
    # - admin: The Admin user object
    """
    while True:
        clear_console()
        print("="*60)
        print(f"{'ADMIN DASHBOARD':^60}")
        print(f"Welcome, {admin.name} ({admin.role})".center(60))
        print("="*60)
        
        print("\n1. Menu Management")
        print("2. Employee Management")
        print("3. Sales & Reports")
        print("4. Restaurant Settings")
        print("5. Return to Main Menu")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            print()
            
            if choice == 1:
                menu_management(restaurant, admin)
            elif choice == 2:
                employee_management(restaurant, admin)
            elif choice == 3:
                sales_reports(restaurant, admin)
            elif choice == 4:
                restaurant_settings(restaurant, admin)
            elif choice == 5:
                print("Returning to main menu...")
                time.sleep(3)
                break
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


def menu_management(restaurant, admin):
    """
    # Function: menu_management
    # Provides interface for managing the restaurant's menu
    #
    # Parameters:
    # - restaurant: The Restaurant object
    # - admin: The Admin user object
    """
    while True:
        clear_console()
        print("="*60)
        print(f"{'MENU MANAGEMENT':^60}")
        print("="*60)
        
        print("\n1. View Full Menu")
        print("2. View Menu by Category")
        print("3. Add Menu Item")
        print("4. Remove Menu Item")
        print("5. Update Menu Item")
        print("6. Search Menu Items")
        print("7. Return to Admin Dashboard")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            print()
            
            if choice == 1:
                restaurant.display_menu()
                input("\nPress Enter to continue...")
                
            elif choice == 2:
                # View menu by category
                categories = restaurant.menu.get_item_categories()
                
                print("Available Categories:")
                for i, category in enumerate(categories, 1):
                    print(f"{i}. {category}")
                    
                cat_choice = int(input("\nSelect a category (0 to cancel): "))
                if 0 < cat_choice <= len(categories):
                    restaurant.menu.display_category(categories[cat_choice-1])
                input("\nPress Enter to continue...")
                
            elif choice == 3:
                # Add menu item
                name = input("Enter item name: ")
                
                # Check if item already exists
                if restaurant.find_food_item(name):
                    print(f"{name} already exists in the menu.")
                    time.sleep(3)
                    continue
                
                try:
                    price = float(input("Enter item price: $"))
                    quantity = int(input("Enter initial stock quantity: "))
                    
                    # Get additional details
                    category = input("Enter item category (or press Enter for 'Main Course'): ")
                    if not category:
                        category = "Main Course"
                        
                    description = input("Enter item description: ")
                    
                    # Get ingredients
                    ingredients = []
                    print("\nEnter ingredients (leave empty to finish):")
                    while True:
                        ingredient = input("> ")
                        if not ingredient:
                            break
                        ingredients.append(ingredient)
                    
                    # Create and add the food item
                    food_item = FoodItem(
                        name=name, 
                        price=price, 
                        quantity=quantity,
                        category=category,
                        description=description,
                        ingredients=ingredients
                    )
                    
                    admin.add_menu_item(restaurant, food_item)
                    input("\nPress Enter to continue...")
                    
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                    time.sleep(3)
            
            elif choice == 4:
                # Remove menu item
                name = input("Enter item name to remove: ")
                admin.remove_menu_item(restaurant, name)
                input("\nPress Enter to continue...")
            
            elif choice == 5:
                # Update menu item
                name = input("Enter item name to update: ")
                
                item = restaurant.find_food_item(name)
                if item:
                    try:
                        print(f"\nCurrent details for {item.name}:")
                        print(f"Price: ${item.price:.2f}")
                        print(f"Quantity: {item.quantity}")
                        print(f"Category: {item.category}")
                        print(f"Description: {item.description}")
                        print(f"Ingredients: {', '.join(item.ingredients)}")
                        print()
                        
                        # Get updated values
                        new_price_input = input(f"Enter new price (current: ${item.price:.2f}), press Enter to skip: ")
                        new_price = float(new_price_input) if new_price_input else None
                        
                        new_quantity_input = input(f"Enter new quantity (current: {item.quantity}), press Enter to skip: ")
                        new_quantity = int(new_quantity_input) if new_quantity_input else None
                        
                        new_description_input = input(f"Enter new description (current: {item.description}), press Enter to skip: ")
                        new_description = new_description_input if new_description_input else None
                        
                        new_category_input = input(f"Enter new category (current: {item.category}), press Enter to skip: ")
                        new_category = new_category_input if new_category_input else None
                        
                        # Update the menu item
                        restaurant.menu.update_item(
                            name, 
                            new_price=new_price, 
                            new_quantity=new_quantity,
                            new_description=new_description,
                            new_category=new_category
                        )
                        
                        # Option to update ingredients
                        update_ingredients = input("Do you want to update ingredients? (y/n): ").lower()
                        if update_ingredients == 'y':
                            # Clear existing ingredients
                            item.ingredients = []
                            
                            # Add new ingredients
                            print("\nEnter new ingredients (leave empty to finish):")
                            while True:
                                ingredient = input("> ")
                                if not ingredient:
                                    break
                                item.ingredients.append(ingredient)
                            
                            print("Ingredients updated.")
                        
                    except ValueError:
                        print("Invalid input. Please enter valid numbers.")
                    
                    input("\nPress Enter to continue...")
                else:
                    print(f"{name} not found in menu.")
                    time.sleep(3)
            
            elif choice == 6:
                # Search menu items
                keyword = input("Enter search keyword: ")
                found_items = restaurant.menu.search_items(keyword)
                
                if found_items:
                    print(f"\nFound {len(found_items)} items matching '{keyword}':")
                    print()
                    
                    print("=" * 60)
                    print(f"{'Item Name':<20} {'Price':^10} {'Category':<20}")
                    print("-" * 60)

                    for item in found_items:
                        print(f"{item.name:<20} {item.price:^10.2f} {item.category:<20}")
                        print()
                        print(f"Description: {item.description}")
                        print(f"Ingredients: {', '.join(item.ingredients)}")
                        print("=" * 60, "\n")
                        
                else:
                    print(f"No items found matching '{keyword}'.")
                
                input("\nPress Enter to continue...")
            
            elif choice == 7:
                print("Returning to admin dashboard...")
                time.sleep(3)
                break
                
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


def employee_management(restaurant, admin):
    """
    # Function: employee_management
    # Provides interface for managing restaurant employees
    #
    # Parameters:
    # - restaurant: The Restaurant object
    # - admin: The Admin user object
    """
    while True:
        clear_console()
        print("="*60)
        print(f"{'EMPLOYEE MANAGEMENT':^60}")
        print("="*60)
        
        print("\n1. View All Employees")
        print("2. Add Employee")
        print("3. Remove Employee")
        print("4. Update Employee Information")
        print("5. Return to Admin Dashboard")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            print()
            
            if choice == 1:
                admin.display_all_employees(restaurant)
                input("\nPress Enter to continue...")
            
            elif choice == 2:
                # Add employee
                name = input("Enter employee name: ")
                phone = input("Enter employee phone: ")
                email = input("Enter employee email: ")
                address = input("Enter employee address: ")
                
                try:
                    age = int(input("Enter employee age: "))
                    job_title = input("Enter employee job title: ")
                    salary = float(input("Enter employee salary: $"))
                    
                    employee = Employee(name, phone, email, address, age, job_title, salary)
                    admin.add_employee(restaurant, employee)
                    input("\nPress Enter to continue...")
                except ValueError:
                    print("Invalid input. Please enter valid numbers for age and salary.")
                    time.sleep(3)
            
            elif choice == 3:
                # Remove employee
                name = input("Enter employee name to remove: ")
                admin.remove_employee(restaurant, name)
                input("\nPress Enter to continue...")
            
            elif choice == 4:
                # Update employee
                name = input("Enter employee name to update: ")
                employee = restaurant.find_employee(name)
                
                if employee:
                    print(f"\nCurrent details for {employee.name}:")
                    print(f"Phone: {employee.phone}")
                    print(f"Email: {employee.email}")
                    print(f"Address: {employee.address}")
                    print(f"Job Title: {employee.job_title}")
                    print(f"Salary: ${employee.salary:.2f}")
                    print()
                    
                    # Get updated values
                    new_phone = input("Enter new phone (press Enter to skip): ")
                    new_email = input("Enter new email (press Enter to skip): ")
                    new_address = input("Enter new address (press Enter to skip): ")
                    
                    # Update contact info
                    if new_phone or new_email or new_address:
                        employee.update_contact_info(
                            phone=new_phone or None,
                            email=new_email or None,
                            address=new_address or None
                        )
                    
                    # Update job title
                    new_job_title = input("Enter new job title (press Enter to skip): ")
                    if new_job_title:
                        employee.job_title = new_job_title
                    
                    # Update salary
                    new_salary_input = input("Enter new salary (press Enter to skip): ")
                    if new_salary_input:
                        try:
                            new_salary = float(new_salary_input)
                            employee.update_salary(new_salary)
                        except ValueError:
                            print("Invalid salary format. Salary not updated.")
                    
                    print(f"{employee.name}'s information has been updated.")
                else:
                    print(f"No employee named {name} was found.")
                
                input("\nPress Enter to continue...")
            
            elif choice == 5:
                print("Returning to admin dashboard...")
                time.sleep(3)
                break
                
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


def sales_reports(restaurant, admin):
    """
    # Function: sales_reports
    # Provides interface for viewing sales reports
    #
    # Parameters:
    # - restaurant: The Restaurant object
    # - admin: The Admin user object
    """
    while True:
        clear_console()
        print("="*60)
        print(f"{'SALES & REPORTS':^60}")
        print("="*60)
        
        print("\n1. View Total Revenue")
        print("2. View Daily Revenue")
        print("3. View All Orders")
        print("4. View Orders by Status")
        print("5. Export Daily Report")
        print("6. Return to Admin Dashboard")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            print()
            
            if choice == 1:
                # View total revenue
                admin.view_revenue(restaurant)
                input("\nPress Enter to continue...")
            
            elif choice == 2:
                # View daily revenue
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
                
                if date_input:
                    try:
                        date = datetime.strptime(date_input, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Using today's date.")
                        date = datetime.now().date()
                else:
                    date = datetime.now().date()
                
                daily_revenue = restaurant.get_daily_revenue(date)
                print(f"\nRevenue for {date}: ${daily_revenue:.2f}")
                input("\nPress Enter to continue...")
            
            elif choice == 3:
                # View all orders
                if not restaurant.orders:
                    print("No orders to display.")
                else:
                    print("\n" + "="*70)
                    print("All Orders")
                    print("-"*70)
                    print(f"{'Order ID':<25}{'Status':<12}{'Items':<8}{'Total':<10}{'Time':<20}")
                    print("-"*70)
                    for order in restaurant.orders:
                        print(f"{order.order_id:<25}{order.status:<12}{order.item_count():<8}${order.calculate_total_price():<9.2f}{str(order.order_time)[:19]:<20}")
                    print("="*70)
                
                input("\nPress Enter to continue...")
            
            elif choice == 4:
                # View orders by status
                print("\nOrder Statuses:")
                for i, status in enumerate(["Placed", "Preparing", "Ready", "Delivered", "Cancelled"], 1):
                    print(f"{i}. {status}")
                
                status_choice = int(input("\nSelect a status (0 to cancel): "))
                if 1 <= status_choice <= 5:
                    status = ["Placed", "Preparing", "Ready", "Delivered", "Cancelled"][status_choice-1]
                    orders = restaurant.get_orders_by_status(status)
                    
                    if not orders:
                        print(f"No {status} orders to display.")
                    else:
                        print("\n" + "="*70)
                        print(f"{status} Orders")
                        print("-"*70)
                        print(f"{'Order ID':<25}{'Items':<8}{'Total':<10}{'Time':<20}")
                        print("-"*70)
                        for order in orders:
                            print(f"{order.order_id:<25}{order.item_count():<8}${order.calculate_total_price():<9.2f}{str(order.order_time)[:19]:<20}")
                        print("="*70)
                
                input("\nPress Enter to continue...")
            
            elif choice == 5:
                # Export daily report
                date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
                
                if date_input:
                    try:
                        date = datetime.strptime(date_input, "%Y-%m-%d").date()
                    except ValueError:
                        print("Invalid date format. Using today's date.")
                        date = datetime.now().date()
                else:
                    date = datetime.now().date()
                
                restaurant.export_daily_report(date)
                input("\nPress Enter to continue...")
            
            elif choice == 6:
                print("Returning to admin dashboard...")
                time.sleep(3)
                break
                
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


def restaurant_settings(restaurant, admin):
    """
    # Function: restaurant_settings
    # Provides interface for configuring restaurant settings
    #
    # Parameters:
    # - restaurant: The Restaurant object
    # - admin: The Admin user object
    """
    while True:
        clear_console()
        print("="*60)
        print(f"{'RESTAURANT SETTINGS':^60}")
        print("="*60)
        
        print("\n1. Update Restaurant Information")
        print("2. Manage Tables")
        print("3. Update Opening Hours")
        print("4. Return to Admin Dashboard")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            print()
            
            if choice == 1:
                # Update restaurant information
                print("Current Information:")
                print(f"Name: {restaurant.name}")
                print(f"Address: {restaurant.address}")
                print(f"Phone: {restaurant.phone}")
                
                print("\nLeave fields blank to keep current values.\n")
                new_name = input("New name: ")
                new_address = input("New address: ")
                new_phone = input("New phone: ")
                
                if new_name:
                    restaurant.name = new_name
                if new_address:
                    restaurant.address = new_address
                if new_phone:
                    restaurant.phone = new_phone
                    
                print("Restaurant information updated.")
                input("\nPress Enter to continue...")
            
            elif choice == 2:
                # Manage tables
                manage_tables(restaurant)
            
            elif choice == 3:
                # Update opening hours
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                
                print("Current Opening Hours:")
                for day in days:
                    hours = restaurant.opening_hours[day]
                    print(f"{day}: {hours['open']} - {hours['close']}")
                
                print("\nSelect day to update:")
                for i, day in enumerate(days, 1):
                    print(f"{i}. {day}")
                
                day_choice = int(input("\nEnter choice (0 to cancel): "))
                if 1 <= day_choice <= 7:
                    day = days[day_choice-1]
                    
                    open_time = input(f"Enter opening time (HH:MM) for {day}: ")
                    close_time = input(f"Enter closing time (HH:MM) for {day}: ")
                    
                    restaurant.update_opening_hours(day, open_time, close_time)
                
                input("\nPress Enter to continue...")
            
            elif choice == 4:
                print("Returning to admin dashboard...")
                time.sleep(3)
                break
                
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


def employee_login(restaurant):
    """
    # Function: employee_login
    # Provides login interface for employees
    #
    # Parameters:
    # - restaurant: The Restaurant object
    """
    clear_console()
    print("="*60)
    print(f"{'EMPLOYEE LOGIN':^60}")
    print("="*60)
    
    name = input("\nEnter your name: ")
    
    # Find employee by name
    employee = restaurant.find_employee(name)
    
    if not employee:
        print(f"No employee named {name} found.")
        time.sleep(3)
        return
    
    print(f"\nWelcome, {employee.name}!")
    employee.record_login()  # Record the login time
    time.sleep(3)
    
    employee_menu(restaurant, employee)


def employee_menu(restaurant, employee):
    """
    # Function: employee_menu
    # Provides the employee interface for managing orders
    #
    # Parameters:
    # - restaurant: The Restaurant object
    # - employee: The Employee user object
    """
    while True:
        clear_console()
        print("="*60)
        print(f"{'EMPLOYEE DASHBOARD':^60}")
        print(f"Welcome, {employee.name} ({employee.job_title})".center(60))
        print("="*60)
        
        print("\n1. View Pending Orders")
        print("2. Mark Order as Ready")
        print("3. Mark Order as Delivered")
        print("4. View All Orders")
        print("5. View Menu")
        print("6. View My Profile")
        print("7. Return to Main Menu")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            print()
            
            if choice == 1:
                # View pending orders (not delivered)
                employee.view_pending_orders(restaurant)
                input("\nPress Enter to continue...")
            
            elif choice == 2:
                # Mark order as ready
                order_id = input("Enter order ID to mark as ready: ")
                if employee.mark_order_ready(restaurant, order_id):
                    print(f"Order {order_id} has been marked as ready.")
                input("\nPress Enter to continue...")
            
            elif choice == 3:
                # Mark order as delivered
                order_id = input("Enter order ID to mark as delivered: ")
                if employee.mark_order_delivered(restaurant, order_id):
                    print(f"Order {order_id} has been marked as delivered.")
                input("\nPress Enter to continue...")
            
            elif choice == 4:
                # View all orders
                if not restaurant.orders:
                    print("No orders to display.")
                else:
                    print("\n" + "="*70)
                    print("All Orders")
                    print("-"*70)
                    print(f"{'Order ID':<25}{'Status':<12}{'Items':<8}{'Total':<10}{'Time':<20}")
                    print("-"*70)
                    for order in restaurant.orders:
                        print(f"{order.order_id:<25}{order.status:<12}{order.item_count():<8}${order.calculate_total_price():<9.2f}{str(order.order_time)[:19]:<20}")
                    print("="*70)
                input("\nPress Enter to continue...")
            
            elif choice == 5:
                # View menu
                restaurant.display_menu()
                input("\nPress Enter to continue...")
            
            elif choice == 6:
                # View profile
                employee.display_info()
                input("\nPress Enter to continue...")
            
            elif choice == 7:
                print("Returning to main menu...")
                time.sleep(3)
                break
            
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


def customer_menu(restaurant):
    """
    # Function: customer_menu
    # Provides the customer interface for ordering food
    #
    # Parameters:
    # - restaurant: The Restaurant object
    """
    clear_console()
    print("="*60)
    print(f"{'CUSTOMER INTERFACE':^60}")
    print("="*60)
    
    # Check if restaurant is open
    if not restaurant.is_open():
        print(f"\nSorry, {restaurant.name} is currently closed.")
        day = datetime.now().strftime("%A")
        hours = restaurant.opening_hours[day]
        print(f"Opening hours for today: {hours['open']} - {hours['close']}")
        
        enter_anyway = input("\nDo you want to continue anyway? (y/n): ").lower()
        if enter_anyway != 'y':
            time.sleep(3)
            return
    
    # Get customer details
    print("\nPlease provide your information:")
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    
    customer = Customer(name=name, phone=phone, email=email, address=address)
    
    while True:
        clear_console()
        print("="*60)
        print(f"{'CUSTOMER DASHBOARD':^60}")
        print(f"Welcome, {customer.name} to {restaurant.name}".center(60))
        print("="*60)
        
        print("\n1. Browse Menu")
        print("2. Search Menu")
        print("3. Add Item to Cart")
        print("4. View Cart")
        print("5. Remove Item from Cart")
        print("6. Update Item Quantity")
        print("7. Add Special Instructions")
        print("8. Place Order")
        print("9. View Order History")
        print("10. View My Profile")
        print("11. Return to Main Menu")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            print()
            
            if choice == 1:
                # Browse menu
                print("\n1. View Full Menu")
                print("2. View Menu by Category")
                
                browse_choice = int(input("\nEnter choice: "))
                
                if browse_choice == 1:
                    customer.view_menu(restaurant)
                elif browse_choice == 2:
                    categories = restaurant.menu.get_item_categories()
                    
                    print("\nAvailable Categories:")
                    for i, category in enumerate(categories, 1):
                        print(f"{i}. {category}")
                        
                    cat_choice = int(input("\nSelect a category (0 to cancel): "))
                    if 0 < cat_choice <= len(categories):
                        customer.view_category(restaurant, categories[cat_choice-1])
                else:
                    print("Invalid choice.")
                
                input("\nPress Enter to continue...")
            
            elif choice == 2:
                # Search menu
                keyword = input("Enter search keyword: ")
                customer.search_menu(restaurant, keyword)
                input("\nPress Enter to continue...")
            
            elif choice == 3:
                # Add item to cart
                item_name = input("What would you like to order? ")
                
                # Check if item exists
                item = restaurant.find_food_item(item_name)
                if item:
                    try:
                        quantity = int(input(f"How many {item_name}s would you like? "))
                        if quantity <= 0:
                            print("Quantity must be positive.")
                        else:
                            customer.add_item_to_cart(restaurant, item_name, quantity)
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print(f"Sorry, we don't have {item_name} on our menu.")
                
                input("\nPress Enter to continue...")
            
            elif choice == 4:
                # View cart
                customer.view_cart()
                input("\nPress Enter to continue...")
            
            elif choice == 5:
                # Remove item from cart
                item_name = input("Enter the name of the item you want to remove: ")
                customer.remove_item_from_cart(restaurant, item_name)
                input("\nPress Enter to continue...")
            
            elif choice == 6:
                # Update item quantity
                item_name = input("Enter the item name: ")
                
                # Check if item exists and is in cart
                item = restaurant.find_food_item(item_name)
                if item and item in customer.cart.items:
                    try:
                        new_quantity = int(input(f"Enter new quantity (current: {customer.cart.items[item]}): "))
                        customer.update_cart_item_quantity(restaurant, item_name, new_quantity)
                    except ValueError:
                        print("Please enter a valid number.")
                else:
                    print(f"{item_name} not found in your cart.")
                
                input("\nPress Enter to continue...")
            
            elif choice == 7:
                # Add special instructions
                instructions = input("Enter any special instructions for your order: ")
                customer.add_special_instructions(instructions)
                input("\nPress Enter to continue...")
            
            elif choice == 8:
                # Place order
                if customer.cart.is_empty():
                    print("Your cart is empty. Add some items before placing an order.")
                else:
                    print("\nOrder Summary:")
                    customer.view_cart()
                    
                    # Choose order type
                    print("\nOrder Type:")
                    print("1. Delivery")
                    print("2. Dine-in")
                    print("3. Pickup")
                    
                    try:
                        order_type = int(input("\nSelect order type: "))
                        
                        delivery_address = None
                        table_number = None
                        
                        if order_type == 1:
                            # Delivery
                            use_default = input(f"Use your address ({customer.address}) for delivery? (y/n): ").lower()
                            if use_default != 'y':
                                delivery_address = input("Enter delivery address: ")
                            else:
                                delivery_address = customer.address
                                
                        elif order_type == 2:
                            # Dine-in
                            party_size = int(input("How many people in your party? "))
                            
                            # Find available table
                            table = restaurant.find_available_table(party_size)
                            
                            if table:
                                table_number = table['number']
                                print(f"You have been assigned to Table {table_number}.")
                                restaurant.set_table_status(table_number, "Reserved")
                            else:
                                print("Sorry, no suitable tables available. Please choose another order type.")
                                input("\nPress Enter to continue...")
                                continue
                                
                        # Payment method
                        print("\nPayment Method:")
                        print("1. Cash")
                        print("2. Credit Card")
                        print("3. Mobile Payment")
                        
                        payment_choice = int(input("\nSelect payment method: "))
                        
                        payment_method = {
                            1: "Cash",
                            2: "Credit Card",
                            3: "Mobile Payment"
                        }.get(payment_choice, "Cash")
                        
                        # Place the order
                        order = customer.place_order(
                            payment_method=payment_method,
                            delivery_address=delivery_address,
                            table_number=table_number
                        )
                        
                        if order:
                            print("Order placed successfully!")
                            print(f"Your order ID is: {order.order_id}")
                            
                            # Simulate order processing by restaurant
                            restaurant.process_order(order)
                        
                    except ValueError:
                        print("Invalid input. Please enter valid numbers.")
                
                input("\nPress Enter to continue...")
            
            elif choice == 9:
                # View order history
                customer.view_order_history()
                input("\nPress Enter to continue...")
            
            elif choice == 10:
                # View profile
                customer.display_info()
                input("\nPress Enter to continue...")
            
            elif choice == 11:
                print("Returning to main menu...")
                time.sleep(3)
                break
            
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


def manage_tables(restaurant):
    """
    # Function: manage_tables
    # Interface for managing restaurant tables
    #
    # Parameters:
    # - restaurant: The Restaurant object
    """
    while True:
        clear_console()
        print("="*60)
        print(f"{'TABLE MANAGEMENT':^60}")
        print("="*60)
        
        print("\nCurrent Tables:")
        if not restaurant.tables:
            print("No tables configured.")
        else:
            print(f"{'Table #':<10}{'Capacity':<10}{'Status':<15}")
            print("-"*35)
            for table in sorted(restaurant.tables, key=lambda t: t['number']):
                print(f"{table['number']:<10}{table['capacity']:<10}{table['status']:<15}")
        
        print("\n1. Add New Table")
        print("2. Change Table Status")
        print("3. Return to Settings")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                # Add new table
                try:
                    table_number = int(input("Enter table number: "))
                    capacity = int(input("Enter seating capacity: "))
                    
                    restaurant.add_table(table_number, capacity)
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                
                input("\nPress Enter to continue...")
            
            elif choice == 2:
                # Change table status
                try:
                    table_number = int(input("Enter table number: "))
                    
                    # Find the table
                    table = None
                    for t in restaurant.tables:
                        if t['number'] == table_number:
                            table = t
                            break
                    
                    if table:
                        print(f"\nCurrent status: {table['status']}")
                        print("\nAvailable statuses:")
                        print("1. Available")
                        print("2. Occupied")
                        print("3. Reserved")
                        
                        status_choice = int(input("\nSelect new status: "))
                        
                        if status_choice == 1:
                            restaurant.set_table_status(table_number, "Available")
                        elif status_choice == 2:
                            restaurant.set_table_status(table_number, "Occupied")
                        elif status_choice == 3:
                            restaurant.set_table_status(table_number, "Reserved")
                        else:
                            print("Invalid choice.")
                    else:
                        print(f"Table {table_number} not found.")
                except ValueError:
                    print("Invalid input. Please enter valid numbers.")
                
                input("\nPress Enter to continue...")
            
            elif choice == 3:
                break
                
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
                
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


def main():
    """
    # Function: main
    # The main function that runs the restaurant management system
    # This initializes the restaurant, creates sample data, and runs the main menu
    """
    # Clear the console
    clear_console()
    
    # Initialize restaurant (create an instance of the Restaurant class)
    restaurant = Restaurant(
        name="Djini's Bakehouse", 
        address="Anyelir 2 st AB 15 A Kemang Pratama 2 Bekasi",
        phone="+62-838-555-022"
    )
    
    # Initialize data directory
    init_data_directory()
    
    # Add sample food items (create instances of FoodItem)
    print("Initializing menu...")
    initialize_menu(restaurant)
    
    # Create tables
    print("Setting up tables...")
    initialize_tables(restaurant)
    
    # Add sample admin (create an instance of Admin)
    admin = Admin(
        name="Safira ajrina husna", 
        phone="+62-838-555-022", 
        email="s.husna@restaurant.com", 
        address="Anyelir 2 st AB 15 A Kemang Pratama 2 Bekasi"
    )

    # Add sample employees (create instances of Employee)
    print("Hiring staff...")
    chef = Employee(
        name="Hasan", 
        phone="01811-987654", 
        email="hasan.chef@restaurant.com", 
        address="Mirpur-10, Dhaka", 
        age=30, 
        job_title="Chef", 
        salary=50000
    )
    server = Employee(
        name="Sumi", 
        phone="01922-456789", 
        email="sumi.server@restaurant.com", 
        address="Gulshan-2, Dhaka", 
        age=24, 
        job_title="Server", 
        salary=30000
    )
    cashier = Employee(
        name="Karim", 
        phone="01733-111222", 
        email="karim.cashier@restaurant.com", 
        address="Uttara, Dhaka", 
        age=27, 
        job_title="Cashier", 
        salary=35000
    )
    
    # Add employees to the restaurant
    admin.add_employee(restaurant, chef)
    admin.add_employee(restaurant, server)
    admin.add_employee(restaurant, cashier)
    
    print("Restaurant system initialized successfully!")
    time.sleep(3)
    
    # Main program loop
    while True:
        clear_console()
        print("\n" + "="*60)
        print(f"{restaurant.name}".center(60))
        print(f"{restaurant.address}".center(60))
        print(f"{restaurant.phone}".center(60))
        print("="*60)
        print(f"{'MAIN MENU':^60}")
        print("="*60)
        print("1. Admin Login")
        print("2. Employee Login")
        print("3. Customer Access")
        print("4. Exit")
        print("-"*60)
        
        try:
            choice = int(input("Enter your choice: "))
            print()
            
            if choice == 1:
                admin_menu(restaurant, admin)
            elif choice == 2:
                employee_login(restaurant)
            elif choice == 3:
                customer_menu(restaurant)
            elif choice == 4:
                print("Thank you for using our system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                time.sleep(3)
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(3)
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(3)


if __name__ == "__main__":
    """
    # Program Entry Point
    # This is where the program execution begins when run as a script
    """
    try:
        main()  # Call the main function to start the program
    except KeyboardInterrupt:
        # Handle keyboard interrupt (Ctrl+C)
        print("\nProgram terminated by user.")
    except Exception as e:
        # Handle any unexpected exceptions
        print(f"\nAn unexpected error occurred: {e}")
        input("\nPress Enter to exit...")