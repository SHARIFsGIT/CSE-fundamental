class Phone:
    manufacturer = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, number, message):
        text = f'sending to {number} {message}'
        print(text)

my_phone = Phone('Sharif', 'OnePlus', 50000)
print(my_phone.owner, my_phone.brand, my_phone.price)

her_phone = Phone('Safira', 'iPhone', 120000)
print(her_phone.owner, her_phone.brand, her_phone.price)

my_phone.send_sms('0123456789', 'Hello, how are you?')
her_phone.send_sms('987456', 'Hello, love you.')