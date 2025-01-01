# Define a function named `double_decker`
def double_decker():
    # Print a message indicating this is the outer function
    print('I am a double decker function')
    
    # Define a nested function named `single_decker`
    def single_decker():
        # Print a message indicating this is the inner function
        print('I am a single decker function')
        # Return a string from the inner function
        return 'Hello from single_decker'
    
    # Return the reference to the inner function
    return single_decker

# Call the `double_decker` function and print its return value
# This will return the `single_decker` function itself (not call it yet)
print(double_decker())

# Call the `double_decker` function and immediately call the returned `single_decker` function
# This will execute both `double_decker` and `single_decker`
print(double_decker()())

# Define a function named `do_something` that takes another function as an argument
def do_something(work):
    print('Work started')  # Print a message indicating work is starting
    # Uncommenting the line below would display the argument passed to `work`
    # print(work)
    work()  # Call the function passed as `work`
    print('Work ended')  # Print a message indicating work has ended

# Uncommenting the lines below would cause errors because integers or strings are not callable
# do_something(2)
# do_something('Hello')

# Define a function named `coding`
def coding():
    print('Coding started')  # Print a message indicating coding has started

# Pass the `coding` function as an argument to `do_something`
do_something(coding)

# Define another function named `sleeping`
def sleeping():
    print('Sleeping started')  # Print a message indicating sleeping has started

# Pass the `sleeping` function as an argument to `do_something`
do_something(sleeping)