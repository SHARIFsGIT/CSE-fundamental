class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        product = {'item': item, 'price': price, 'quantity': quantity}
        self.cart.append(product)

    def check_out(self, amount):
        total_pay = sum(item['price'] * item['quantity'] for item in self.cart)
        print('Total payable amount:', total_pay)
        print('You paid:', amount)
        if amount < total_pay:
            print(f'Please provide {total_pay - amount} more')
        else:
            extra_amount = amount - total_pay
            print('Thank you for your purchase. Your change is:', extra_amount)

    def remove_from_cart(self, item):
        for i, product in enumerate(self.cart):
            if product['item'] == item:
                print(f'{item} has been removed')
                del self.cart[i]
                return
        print(f'{item} is not in the cart')

user1 = Shopping('user1')
user1.add_to_cart('Laptop', 50, 2)
user1.add_to_cart('Phone', 10, 5)
user1.remove_from_cart('Phone')

print(user1.cart)

user1.check_out(60)