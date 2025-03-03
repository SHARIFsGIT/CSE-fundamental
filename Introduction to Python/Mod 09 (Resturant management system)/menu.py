# -------------------- Menu Class --------------------
"""
This module defines the Menu class for the restaurant management system.
The Menu class manages the collection of food items offered by the restaurant.
"""

class Menu:
    """
    # Class: Menu
    # Purpose: Represents the restaurant's menu, containing food items
    #
    # Properties:
    # - items: List of FoodItem objects in the menu
    # - categories: Dictionary mapping category names to lists of FoodItem objects
    """
    def __init__(self):
        """
        # Constructor
        # Initializes a new instance of the Menu class
        """
        # Instance attributes/properties
        self.items = []  # List to store all food items
        self.categories = {}  # Dictionary to organize items by category
        
        # Creating standard menu categories
        self.standard_categories = [
            "Appetizers", "Main Course", "Desserts", 
            "Beverages", "Specials", "Soups", "Salads"
        ]
        
        # Initialize the categories dictionary with empty lists
        for category in self.standard_categories:
            self.categories[category] = []

    def add_item(self, item):
        """
        # Method: add_item
        # Adds a food item to the menu
        #
        # Parameters:
        # - item: The FoodItem object to add
        #
        # Returns:
        # - bool: True if added successfully, False otherwise
        """
        # Check if item with same name already exists (case insensitive)
        existing_item = self.find_item(item.name)
        if existing_item:
            print(f"{item.name} already exists in the menu. Please update it instead.")
            return False
        
        # Add to the main items list
        self.items.append(item)
        
        # Add to the appropriate category
        if item.category in self.categories:
            self.categories[item.category].append(item)
        else:
            # Create a new category if it doesn't exist
            self.categories[item.category] = [item]
            
        print(f"{item.name} has been added to the menu under {item.category}.")
        return True

    def find_item(self, item_name):
        """
        # Method: find_item
        # Finds a food item by name (case insensitive)
        #
        # Parameters:
        # - item_name: The name of the item to find
        #
        # Returns:
        # - FoodItem: The found item or None if not found
        """
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        """
        # Method: remove_item
        # Removes a food item from the menu by name
        #
        # Parameters:
        # - item_name: The name of the item to remove
        #
        # Returns:
        # - bool: True if removed successfully, False if not found
        """
        item = self.find_item(item_name)
        if item:
            # Remove from the main items list
            self.items.remove(item)
            
            # Remove from the category list
            if item.category in self.categories:
                if item in self.categories[item.category]:
                    self.categories[item.category].remove(item)
            
            print(f"{item.name} has been removed from the menu.")
            return True
        else:
            print(f"{item_name} is not found in the menu.")
            return False

    def update_item(self, item_name, new_price=None, new_quantity=None, new_description=None, new_category=None):
        """
        # Method: update_item
        # Updates a food item's properties
        #
        # Parameters:
        # - item_name: The name of the item to update
        # - new_price: The new price (optional)
        # - new_quantity: The new quantity (optional)
        # - new_description: The new description (optional)
        # - new_category: The new category (optional)
        #
        # Returns:
        # - bool: True if updated successfully, False if not found
        """
        item = self.find_item(item_name)
        if not item:
            print(f"{item_name} is not found in the menu.")
            return False
        
        # Update properties if provided
        if new_price is not None:
            item.price = new_price
        
        if new_quantity is not None:
            item.quantity = new_quantity
            
        if new_description is not None:
            item.description = new_description
            
        if new_category is not None and new_category != item.category:
            # Remove from old category
            if item.category in self.categories:
                if item in self.categories[item.category]:
                    self.categories[item.category].remove(item)
            
            # Update the category
            item.category = new_category
            
            # Add to new category
            if new_category in self.categories:
                self.categories[new_category].append(item)
            else:
                self.categories[new_category] = [item]
            
        print(f"{item.name} has been updated.")
        return True

    def display_menu(self):
        """
        # Method: display_menu
        # Displays all items in the menu with their details
        # Organizes display by category
        """
        if not self.items:
            print("The menu is currently empty.")
            return

        print("\n" + "="*70)
        print(f"{'RESTAURANT MENU':^70}")
        print("="*70)
        
        # Display menu by category
        for category in sorted(self.categories.keys()):
            if not self.categories[category]:
                continue  # Skip empty categories
                
            print(f"\n{category.upper()}")
            print("-"*70)
            print(f"{'Item Name':<30}{'Price':^10}{'Stock':^10}{'Description':<20}")
            print("-"*70)
            
            for item in sorted(self.categories[category], key=lambda x: x.name):
                # Show discounted price if applicable
                if item.discount_percentage > 0:
                    price_display = f"${item.get_discounted_price():.2f} (${item.price:.2f})"
                else:
                    price_display = f"${item.price:.2f}"
                    
                description = item.description[:20] + "..." if len(item.description) > 20 else item.description
                print(f"{item.name:<30}{price_display:<15}{item.quantity:^5}{description:<20}")
                
        print("="*70 + "\n")

    def display_category(self, category):
        """
        # Method: display_category
        # Displays all items in a specific category
        #
        # Parameters:
        # - category: The category to display
        """
        if category not in self.categories or not self.categories[category]:
            print(f"No items found in the {category} category.")
            return
            
        print("\n" + "="*70)
        print(f"{category.upper()}")
        print("-"*70)
        print(f"{'Item Name':<30}{'Price':^10}{'Stock':^10}{'Description':<20}")
        print("-"*70)
        
        for item in sorted(self.categories[category], key=lambda x: x.name):
            # Show discounted price if applicable
            if item.discount_percentage > 0:
                price_display = f"${item.get_discounted_price():.2f} (${item.price:.2f})"
            else:
                price_display = f"${item.price:.2f}"
                
            description = item.description[:20] + "..." if len(item.description) > 20 else item.description
            print(f"{item.name:<30}{price_display:<15}{item.quantity:^5}{description:<20}")
            
        print("="*70 + "\n")

    def get_item_categories(self):
        """
        # Method: get_item_categories
        # Returns a list of all categories in the menu
        #
        # Returns:
        # - list: List of category names
        """
        return sorted(self.categories.keys())
        
    def search_items(self, keyword):
        """
        # Method: search_items
        # Searches for items containing the keyword in name or description
        #
        # Parameters:
        # - keyword: The search keyword
        #
        # Returns:
        # - list: List of matching FoodItem objects
        """
        keyword = keyword.lower()
        results = []
        
        for item in self.items:
            if (keyword in item.name.lower() or 
                keyword in item.description.lower() or
                any(keyword in ingredient.lower() for ingredient in item.ingredients)):
                results.append(item)
                
        return results
        
    def get_items_by_price_range(self, min_price, max_price):
        """
        # Method: get_items_by_price_range
        # Returns items within a specific price range
        #
        # Parameters:
        # - min_price: The minimum price
        # - max_price: The maximum price
        #
        # Returns:
        # - list: List of FoodItem objects in the price range
        """
        return [item for item in self.items 
                if min_price <= item.price <= max_price]