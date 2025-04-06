"""
E-Shopping App

A simple object-oriented e-shopping application that demonstrates OOP principles:
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

This application allows:
- Customers to create accounts, browse products, add to cart, and place orders
- Sellers to create accounts, publish and manage products
- Stock management when orders are placed
"""

from services.auth_service import AuthService
from services.product_service import ProductService
from services.order_service import OrderService
from models.user import Customer, Seller
import platform
import subprocess


def clear_console():
    """
    Clear the console screen in a more robust and platform-independent way.
    This implementation avoids potential security issues with os.system().
    """
    if platform.system() == "Windows":
        # For Windows, use the cls command with subprocess for better security
        subprocess.run(["cls"], shell=True, check=False)
    else:
        # For Unix/Linux/MacOS
        # Use ANSI escape sequence which works on most terminals
        print("\033[H\033[J", end="")


class EShoppingApp:
    """
    Main application class that ties all components together.
    
    This class demonstrates the Facade pattern by providing a simplified
    interface to the complex subsystem of services and models.
    """
    
    def __init__(self):
        """Initialize the e-shopping application."""
        self.auth_service = AuthService()
        self.product_service = ProductService()
        self.order_service = OrderService()
        self.current_user_id = None
    
    def start(self):
        """Start the application and show the main menu."""
        clear_console()
        print("\n===== Welcome to E-Shopping App =====\n")
        self._show_main_menu()
    
    def _show_main_menu(self):
        """Display the main menu options."""
        while True:
            print("\n===== Main Menu =====")
            print("1. Register as Customer")
            print("2. Register as Seller")
            print("3. Login")
            print("4. Browse Products (no login required)")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            clear_console()
            
            if choice == "1":
                self._register_customer()
            elif choice == "2":
                self._register_seller()
            elif choice == "3":
                self._login()
            elif choice == "4":
                self._browse_products()
            elif choice == "5":
                print("\nThank you for using E-Shopping App. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
    
    def _register_customer(self):
        """Register a new customer."""
        print("\n===== Register as Customer =====")
        email = input("Enter email: ")
        password = input("Enter password: ")
        name = input("Enter full name: ")
        
        success, message, user_id = self.auth_service.register_customer(email, password, name)
        print(f"\n{message}")
        
        if success:
            self.current_user_id = user_id
            clear_console()
            self._show_customer_menu()
    
    def _register_seller(self):
        """Register a new seller."""
        print("\n===== Register as Seller =====")
        email = input("Enter email: ")
        password = input("Enter password: ")
        name = input("Enter full name: ")
        
        success, message, user_id = self.auth_service.register_seller(email, password, name)
        print(f"\n{message}")
        
        if success:
            self.current_user_id = user_id
            clear_console()
            self._show_seller_menu()
    
    def _login(self):
        """Login with email and password."""
        print("\n===== Login =====")
        email = input("Enter email: ")
        password = input("Enter password: ")
        
        success, message, user_id = self.auth_service.login(email, password)
        print(f"\n{message}")
        
        if success:
            self.current_user_id = user_id
            clear_console()
            
            if self.auth_service.is_customer(user_id):
                self._show_customer_menu()
            elif self.auth_service.is_seller(user_id):
                self._show_seller_menu()
    
    def _show_customer_menu(self):
        """Display the customer menu options."""
        customer = self.auth_service.get_user(self.current_user_id)
        
        while True:
            print(f"\n===== Customer Menu ({customer.name}) =====")
            print("1. Browse Products")
            print("2. View Cart")
            print("3. Checkout")
            print("4. View Order History")
            print("5. Logout")
            
            choice = input("\nEnter your choice (1-5): ")
            
            clear_console()
            
            if choice == "1":
                self._browse_products(allow_add_to_cart=True)
            elif choice == "2":
                self._view_cart(customer)
            elif choice == "3":
                self._checkout(customer)
            elif choice == "4":
                self._view_order_history(customer)
            elif choice == "5":
                self.current_user_id = None
                print("\nLogged out successfully.")
                break
            else:
                print("\nInvalid choice. Please try again.")
    
    def _show_seller_menu(self):
        """Display the seller menu options."""
        seller = self.auth_service.get_user(self.current_user_id)
        
        while True:
            print(f"\n===== Seller Menu ({seller.name}) =====")
            print("1. Add New Product")
            print("2. View My Products")
            print("3. Update Product")
            print("4. Remove Product")
            print("5. Logout")
            
            choice = input("\nEnter your choice (1-5): ")
            
            clear_console()
            
            if choice == "1":
                self._add_product(seller)
            elif choice == "2":
                self._view_seller_products(seller)
            elif choice == "3":
                self._update_product(seller)
            elif choice == "4":
                self._remove_product(seller)
            elif choice == "5":
                self.current_user_id = None
                print("\nLogged out successfully.")
                break
            else:
                print("\nInvalid choice. Please try again.")
    
    def _browse_products(self, allow_add_to_cart=False):
        """
        Browse all available products.
        
        Args:
            allow_add_to_cart (bool): Whether to allow adding products to cart
        """
        print("\n===== Browse Products =====")
        
        products = self.product_service.get_all_products()
        
        if not products:
            print("No products available.")
            return
        
        print("\nAvailable Products:")
        for i, product in enumerate(products, 1):
            print(f"{i}. {product}")
        
        if allow_add_to_cart:
            while True:
                choice = input("\nEnter product number to add to cart (or 0 to go back): ")
                
                if choice == "0":
                    clear_console()
                    break
                
                try:
                    choice = int(choice)
                    if 1 <= choice <= len(products):
                        customer = self.auth_service.get_user(self.current_user_id)
                        customer.add_to_cart(products[choice - 1])
                        print(f"\n{products[choice - 1].name} added to cart!")
                    else:
                        print("Invalid product number.")
                except ValueError:
                    print("Please enter a number.")
    
    def _view_cart(self, customer):
        """
        View the customer's shopping cart.
        
        Args:
            customer (Customer): The customer whose cart to view
        """
        print("\n===== Your Cart =====")
        
        if not customer.cart:
            print("Your cart is empty.")
            return
        
        total = 0
        for i, product in enumerate(customer.cart, 1):
            print(f"{i}. {product.name} - ${product.price:.2f}")
            total += product.price
        
        print(f"\nTotal: ${total:.2f}")
        
        while True:
            print("\n1. Remove item from cart")
            print("2. Clear cart")
            print("3. Go back")
            
            choice = input("\nEnter your choice (1-3): ")
            
            if choice == "1":
                item_num = input("Enter item number to remove: ")
                try:
                    item_num = int(item_num)
                    if 1 <= item_num <= len(customer.cart):
                        product = customer.cart[item_num - 1]
                        customer.remove_from_cart(product.product_id)
                        print(f"\n{product.name} removed from cart.")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Please enter a number.")
            elif choice == "2":
                customer.clear_cart()
                print("\nCart cleared.")
                break
            elif choice == "3":
                clear_console()
                break
            else:
                print("Invalid choice. Please try again.")
    
    def _checkout(self, customer):
        """
        Process the checkout for a customer.
        
        Args:
            customer (Customer): The customer checking out
        """
        print("\n===== Checkout =====")
        
        if not customer.cart:
            print("Your cart is empty.")
            return
        
        # Display cart contents
        total = 0
        for i, product in enumerate(customer.cart, 1):
            print(f"{i}. {product}")
            total += product.price
        
        print(f"\nTotal: ${total:.2f}")
        
        # Confirm order
        confirm = input("\nConfirm order (yes/no): ")
        
        if confirm.lower() != "yes":
            print("Order canceled.")
            return
        
        # Create the order
        success, message, order_id = self.order_service.create_order(
            customer.user_id, customer.cart)
        
        print(f"\n{message}")
        
        if success:
            # Get the order and add it to customer's history
            order = self.order_service.get_order(order_id)
            customer.add_order_to_history(order)
            
            # Clear the cart
            customer.clear_cart()
            
            print(f"Order #{order_id} placed successfully!")
    
    def _view_order_history(self, customer):
        """
        View a customer's order history.
        
        Args:
            customer (Customer): The customer whose history to view
        """
        print("\n===== Order History =====")
        
        orders = self.order_service.get_customer_orders(customer.user_id)
        
        if not orders:
            print("You have no orders.")
            return
        
        for i, order in enumerate(orders, 1):
            print(f"\nOrder #{i}:")
            print(order)
        
        # View detailed order
        while True:
            choice = input("\nEnter order number to view details (or 0 to go back): ")
            
            if choice == "0":
                clear_console()
                break
            
            try:
                choice = int(choice)
                if 1 <= choice <= len(orders):
                    print("\n" + orders[choice - 1].get_details())
                else:
                    print("Invalid order number.")
            except ValueError:
                print("Please enter a number.")
    
    def _add_product(self, seller):
        """
        Add a new product for a seller.
        
        Args:
            seller (Seller): The seller adding the product
        """
        print("\n===== Add New Product =====")
        
        name = input("Enter product name: ")
        description = input("Enter product description (can not be empty): ")
        
        try:
            price = float(input("Enter product price: $"))
            stock = int(input("Enter initial stock quantity: "))
        except ValueError:
            print("Invalid input for price or stock.")
            return
        
        category = input("Enter product category (or leave empty for 'Uncategorized'): ")
        if not category:
            category = "Uncategorized"
        
        success, message, product_id = self.product_service.add_product(
            name, description, price, stock, seller.user_id, category)
        
        print(f"\n{message}")
        
        if success:
            # Add the product to the seller's products list
            product = self.product_service.get_product(product_id)
            seller.add_product(product)
    
    def _view_seller_products(self, seller):
        """
        View all products published by a seller.
        
        Args:
            seller (Seller): The seller whose products to view
        """
        print("\n===== My Products =====")
        
        if not seller.products:
            print("You have no products.")
            return
        
        for i, product in enumerate(seller.products, 1):
            print(f"{i}. {product}")
            
        input("\nPress Enter to continue...")
        clear_console()
    
    def _update_product(self, seller):
        """
        Update an existing product for a seller.
        
        Args:
            seller (Seller): The seller updating the product
        """
        print("\n===== Update Product =====")
        
        if not seller.products:
            print("You have no products.")
            return
        
        for i, product in enumerate(seller.products, 1):
            print(f"{i}. {product}")
        
        choice = input("\nEnter product number to update (or 0 to go back): ")
        
        if choice == "0":
            clear_console()
            return
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(seller.products):
                product = seller.products[choice - 1]
                
                print("\nWhat would you like to update?")
                print("1. Price")
                print("2. Stock quantity")
                print("3. Category")
                
                update_choice = input("\nEnter your choice (1-3): ")
                
                if update_choice == "1":
                    try:
                        new_price = float(input("Enter new price: $"))
                        success, message = self.product_service.update_product(
                            product.product_id, price=new_price)
                        print(f"\n{message}")
                    except ValueError:
                        print("Invalid price.")
                
                elif update_choice == "2":
                    try:
                        new_stock = int(input("Enter new stock quantity: "))
                        success, message = self.product_service.update_product(
                            product.product_id, stock=new_stock)
                        print(f"\n{message}")
                    except ValueError:
                        print("Invalid stock quantity.")
                
                elif update_choice == "3":
                    new_category = input("Enter new category: ")
                    success, message = self.product_service.update_product(
                        product.product_id, category=new_category)
                    print(f"\n{message}")
                
                else:
                    print("Invalid choice.")
            
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a number.")
    
    def _remove_product(self, seller):
        """
        Remove a product for a seller.
        
        Args:
            seller (Seller): The seller removing the product
        """
        print("\n===== Remove Product =====")
        
        if not seller.products:
            print("You have no products.")
            return
        
        for i, product in enumerate(seller.products, 1):
            print(f"{i}. {product}")
        
        choice = input("\nEnter product number to remove (or 0 to go back): ")
        
        if choice == "0":
            clear_console()
            return
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(seller.products):
                product = seller.products[choice - 1]
                
                confirm = input(f"Are you sure you want to remove '{product.name}'? (yes/no): ")
                
                if confirm.lower() == "yes":
                    success, message = self.product_service.delete_product(product.product_id)
                    
                    if success:
                        seller.remove_product(product.product_id)
                    
                    print(f"\n{message}")
            else:
                print("Invalid product number.")
        except ValueError:
            print("Please enter a number.")


if __name__ == "__main__":
    app = EShoppingApp()
    app.start()