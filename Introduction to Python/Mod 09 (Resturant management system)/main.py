# -------------------- Main Application --------------------
from food_item import FoodItem
from menu import Menu
from order import Order
from restaurent import Restaurant
from user import Admin, Customer, Employee

def main():
    # Initialize restaurant
    restaurant = Restaurant("Djini's Bakehouse")
    
    # Admin
    admin = Admin("Safira", "+62 857-7784-9550", "s.husna@gmail.com", "Bekasi")
    
    while True:
        print("\n" + "="*50)
        print(f"Welcome to {restaurant.name}")
        print("="*50)
        print("1. Admin Login")
        print("2. Customer Access")
        print("3. Exit")
        print("-"*50)
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                admin_menu(restaurant, admin)
            elif choice == 2:
                customer_menu(restaurant)
            elif choice == 3:
                print("Thank you for using our system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def admin_menu(restaurant, admin):
    """Admin menu for managing the restaurant."""
    print("\n" + "="*50)
    print("Admin Dashboard")
    print("="*50)
    
    while True:
        print("\n1. View Menu")
        print("2. Add Menu Item")
        print("3. Remove Menu Item")
        print("4. Update Menu Item")
        print("5. View Employees")
        print("6. Add Employee")
        print("7. Remove Employee")
        print("8. View Revenue")
        print("9. Return to Main Menu")
        print("-"*50)
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                restaurant.display_menu()
            
            elif choice == 2:
                name = input("Enter item name: ")
                price = float(input("Enter item price: $"))
                quantity = int(input("Enter initial stock quantity: "))
                
                food_item = FoodItem(name, price, quantity)
                admin.add_menu_item(restaurant, food_item)
            
            elif choice == 3:
                name = input("Enter item name to remove: ")
                admin.remove_menu_item(restaurant, name)
            
            elif choice == 4:
                name = input("Enter item name to update: ")
                
                item = restaurant.find_food_item(name)
                if item:
                    try:
                        new_price_input = input(f"Enter new price (current: ${item.price:.2f}), press Enter to skip: ")
                        new_price = float(new_price_input) if new_price_input else None
                        
                        new_quantity_input = input(f"Enter new quantity (current: {item.quantity}), press Enter to skip: ")
                        new_quantity = int(new_quantity_input) if new_quantity_input else None
                        
                        admin.update_menu_item(restaurant, name, new_price, new_quantity)
                    except ValueError:
                        print("Invalid input. Please enter valid numbers.")
                else:
                    print(f"{name} not found in menu.")
            
            elif choice == 5:
                admin.display_all_employees(restaurant)
            
            elif choice == 6:
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
                except ValueError:
                    print("Invalid input. Please enter valid numbers for age and salary.")
            
            elif choice == 7:
                name = input("Enter employee name to remove: ")
                admin.remove_employee(restaurant, name)
            
            elif choice == 8:
                admin.view_revenue(restaurant)
            
            elif choice == 9:
                print("Returning to main menu...")
                break
            
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


def customer_menu(restaurant):
    """Customer menu for ordering food."""
    print("\n" + "="*50)
    print("Customer Interface")
    print("="*50)
    
    # Get customer details
    name = input("Enter your name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    
    customer = Customer(name=name, phone=phone, email=email, address=address)
    
    while True:
        print(f"\nWelcome {customer.name} to {restaurant.name}")
        print("\n1. View Menu")
        print("2. Add Item to Cart")
        print("3. View Cart")
        print("4. Remove Item from Cart")
        print("5. Update Item Quantity")
        print("6. Place Order")
        print("7. View Order History")
        print("8. Return to Main Menu")
        print("-"*50)
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                customer.view_menu(restaurant)
            
            elif choice == 2:
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
            
            elif choice == 3:
                customer.view_cart()
            
            elif choice == 4:
                item_name = input("Enter the name of the item you want to remove: ")
                customer.remove_item_from_cart(restaurant, item_name)
            
            elif choice == 5:
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
            
            elif choice == 6:
                order = customer.place_order()
                if order:
                    print("Order placed successfully!")
                    print(f"Your order ID is: {order.order_id}")
                    # Simulate order processing by restaurant
                    restaurant.process_order(order)
            
            elif choice == 7:
                customer.view_order_history()
            
            elif choice == 8:
                print("Returning to main menu...")
                break
            
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()