import math
import time

def timer():
    def inner():
        print('Time starts')
        print('Time ends') 
    return inner

# timer()()

def timer2(func):
    def inner(*args, **kwargs):
        print('Time starts')
        st = time.time()
        # print(func)
        func(*args, **kwargs)
        print('Time ends')
        et = time.time()
        print(f'Time taken: {et - st}')
    return inner

@timer2
def get_factorial(n):
    print('Calculating factorial')
    result = math.factorial(n)
    print(f'The factorial of {n} is {result}')

get_factorial(5)
get_factorial(n = 1500)