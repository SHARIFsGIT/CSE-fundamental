try:
    result = 45/0
except:
    print('Error')
finally:
    print('This code will always run')
print('Done')


try:
    result = 45/5
except:
    print('Error')
finally:
    print('This code will always run')
print('Done')