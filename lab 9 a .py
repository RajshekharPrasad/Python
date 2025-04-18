# lab 9 b lambda
# q 1
def fun():
    print("This is the fun function!")

def disp():
    print("This is the disp function!")

def msg():
    print("This is the msg function!")

# Store the functions in a list
functions = [fun, disp, msg]

# Loop through the list and call each function
for function in functions:
    function()

#q 2
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

# Use map and lambda to add corresponding elements of the two lists
result = list(map(lambda x, y: x + y, list1, list2))

print(result)  # Output: [7, 7, 7, 7, 7, 7]
#q3
import random

# Generate 10 random numbers between -15 and 15
random_numbers = random.sample(range(-15, 16), 10)

# Use map and lambda to get the square of each number
squares = list(map(lambda x: x ** 2, random_numbers))

print(f"Random numbers: {random_numbers}")
print(f"Squares: {squares}")
#q3
import random

# Generate 10 random numbers between -15 and 15
random_numbers = random.sample(range(-15, 16), 10)

# Use map and lambda to get the square of each number
squares = list(map(lambda x: x ** 2, random_numbers))

print(f"Random numbers: {random_numbers}")
print(f"Squares: {squares}")
#q4
lst = ['madam', 'Python', 'malayalam', 12321]

# Filter and print the strings that are palindromes
palindromes = list(filter(lambda x: str(x) == str(x)[::-1], lst))

print(f"Palindromes: {palindromes}")
#q 5
faculty_members = ['John Doe', 'Alexandra Smith', 'Bob', 'Elizabeth', 'Alice Williams']

# Filter out names whose length is more than 8 characters
filtered_names = list(filter(lambda name: len(name) > 8, faculty_members))

print(f"Names with more than 8 characters: {filtered_names}")


