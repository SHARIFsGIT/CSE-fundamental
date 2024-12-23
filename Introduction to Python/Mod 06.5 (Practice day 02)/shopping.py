class Product:
    def __init__(self, product_name, product_price, product_quantity) -> None:
        # Initialize a Product object
        self.product_name = product_name
        self.product_price = product_price
        self.product_quantity = product_quantity

    def __str__(self) -> str:
        return f'Product -> name: {self.product_name}, price: {self.product_price}, quantity: {self.product_quantity}'


class Shop:
    def __init__(self) -> None:
        # Initialize a Shop object with an empty product inventory as a list
        self.inventory = []

    def add_product(self, product):
        # Add a product to the inventory
        for existing_product in self.inventory:
            if existing_product.product_name == product.product_name:
                existing_product.product_quantity += product.product_quantity
                print(f"{product.product_name} updated successfully")
                return
        self.inventory.append(product)
        print(f"New item {product.product_name} added to the inventory")

    def buy_product(self, product_name, requested_quantity):
        # Buy a product from the shop
        for existing_product in self.inventory:
            if existing_product.product_name == product_name:
                if existing_product.product_quantity >= requested_quantity:
                    existing_product.product_quantity -= requested_quantity
                    print(f"Congratulations! You have successfully bought {requested_quantity} unit(s) of {product_name}.")
                    if existing_product.product_quantity == 0:
                        self.inventory.remove(existing_product)
                    return
                else:
                    print(f"Sorry, only {existing_product.product_quantity} unit(s) of {product_name} are available.")
                    return
        print(f"Sorry, {product_name} is not available in the shop.")

    def show_inventory(self):
        # Display all products in the inventory
        if not self.inventory:
            print("The inventory is empty.")
        else:
            for product in self.inventory:
                print(product)


# Example usage
test = Shop()

# Adding products
p1 = Product("Laptop", 1000, 10)
p2 = Product("Phone", 500, 20)
p3 = Product("Phone", 500, 4) 

test.add_product(p1)
test.add_product(p2)
test.add_product(p3)

# Buying products
test.buy_product("Laptop", 2)
test.buy_product("Phone", 25)  # Exceeds available quantity
test.buy_product("Tablet", 1)  # Non-existent product

# Show remaining inventory
test.show_inventory()