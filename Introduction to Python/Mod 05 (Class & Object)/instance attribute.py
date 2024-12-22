class Shop:
    shopping_mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = [] # Instance attribute: unique to each instance
    
    def add_to_cart(self, item):
        self.cart.append(item)

user1 = Shop('Shariful')
user1.add_to_cart('Laptop')
user1.add_to_cart('PhoneBook')

print(user1.cart)

user2 = Shop('Sayang')
user2.add_to_cart('Shirt')
user2.add_to_cart('Watch')

print(user2.cart)