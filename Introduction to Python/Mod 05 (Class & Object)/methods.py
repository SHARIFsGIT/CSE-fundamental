def call():
    print('calling someone...')
    return 'finished'

class Phone:
    price = 2500
    color = 'blue'
    brand = 'samsung'
    features = ['camera', 'speaker', 'wifi']

    def call(self):
        print('calling sayang')

    def sms_send(self, phone, sms):
        text = f'sending sms to {phone} and message {sms}'
        return text

my_phone = Phone()
print(my_phone.price)
print(my_phone.features)
my_phone.call()

sms_result = my_phone.sms_send(4152, 'Hello')
print(sms_result)