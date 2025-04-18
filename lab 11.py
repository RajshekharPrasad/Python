def get_integer_input():
    while True:
        user_input = input("Please enter an integer: ")
        try:
            # Attempt to convert the input into an integer
            user_input = int(user_input)
            return user_input  # If successful, return the integer
        except ValueError:
            # If a ValueError occurs, it means the input wasn't a valid integer
            print("Error: Invalid input. Please enter a valid integer.")

# Call the function and print the result
integer_value = get_integer_input()
print(f"You entered the integer: {integer_value}")
