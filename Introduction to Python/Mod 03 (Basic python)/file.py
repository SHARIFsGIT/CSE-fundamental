# .csv = comma-separated value

with open('test.csv', 'w') as test_file:
    test_file.write('Name,Age,City\n')
    test_file.write('John Doe,30,New York\n')
    test_file.write('Jane Smith,25,Los Angeles\n')

with open('test.csv', 'a') as test_file:
    test_file.write('Name,Age,City\n')
    test_file.write('John Doe,30,New York\n')
    test_file.write('Jane Smith,25,Los Angeles\n')

with open('test.csv', 'r') as test_file:
    text = test_file.read()
    print(text)
