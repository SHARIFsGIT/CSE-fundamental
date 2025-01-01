class Shopping:
    # Static or class attribute
    cart = []
    origin = 'China'

    # Constructor method to initialize the instance attributes
    def __init__(self, name, location) -> None:
        # Instance attributes
        self.name = name
        self.location = location

    def purchase(self, item, price, amount):
        remaining = amount - price
        print(f'{self.name} bought {item} for {price}. {self.name} has {remaining} left in the wallet')

    @staticmethod
    def get_origin(item):
        # Static method to get the origin of the product
        print(f'{item} is from {Shopping.origin}')

    @classmethod
    def add_to_cart(self, item):
        # Class method to add an item to the shared cart
        self.cart.append(item)
        print(f'{item} added to the cart')

""" 
# Attempting to call the purchase method directly using the class. This will raise an error because the method is not designed to be used this way.

Shopping.purchase('Shirt', 1000, 5000)  # Uncommenting this line will throw an error.
 """

# Creating an instance of the Shopping class
shopper = Shopping('Sharif', 'Bremen')

# Calling the purchase method using the instance
shopper.purchase('Shirt', 1000, 5000)

# Adding items to the cart using the instance
shopper.add_to_cart('Shirt')

# Accessing the cart attribute using the class name
Shopping.add_to_cart('Shoes')

# Accessing the origin attribute using the class name
Shopping.get_origin('Shoes')