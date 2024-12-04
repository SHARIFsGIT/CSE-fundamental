balance = 3000 # global variable

def buy_things(item, price):
    global balance
    # balance = 1500 # local variable
    balance = balance - price
    print(f'Balance after buying {item}', balance)
    # print('Balance inside the function', balance)
buy_things('sunglasses', 1000)