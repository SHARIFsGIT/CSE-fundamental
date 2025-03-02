# -------------------- Menu Class --------------------

class Menu:
    """
    Represents the restaurant's menu, containing food items.
    """
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add a food item to the menu."""
        # Check if item with same name already exists
        existing_item = self.find_item(item.name)
        if existing_item:
            print(f"{item.name} already exists in the menu. Please update it instead.")
            return False
        
        self.items.append(item)
        print(f"{item.name} has been added to the menu.")
        return True

    def find_item(self, item_name):
        """Find a food item by name (case insensitive)."""
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        """Remove a food item from the menu by name."""
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print(f"{item.name} has been removed from the menu.")
            return True
        else:
            print(f"{item_name} is not found in the menu.")
            return False

    def update_item(self, item_name, new_price=None, new_quantity=None):
        """Update a food item's price and/or quantity."""
        item = self.find_item(item_name)
        if not item:
            print(f"{item_name} is not found in the menu.")
            return False
        
        if new_price is not None:
            item.price = new_price
        
        if new_quantity is not None:
            item.quantity = new_quantity
            
        print(f"{item.name} has been updated.")
        return True

    def display_menu(self):
        """Display all items in the menu with their details."""
        if not self.items:
            print("The menu is currently empty.")
            return

        print("\n" + "="*50)
        print(f"{'Item Name':<30}{'Price':^10}{'Stock':^10}")
        print("-"*50)
        for item in self.items:
            print(f"{item.name:<30}${item.price:<9.2f}{item.quantity:^10}")
        print("="*50 + "\n")

    def get_item_categories(self):
        """Get a list of all categories if they exist."""
        # This is for future expansion if you add categories to FoodItem
        return []