#Print all alphabets first in upper and next lower case each separated by space

def print_alphabets():
  for i in range(65, 91):
    print(chr(i), end=" ")
  print("\n")
  for i in range(65, 91):
    print(chr(i+32), end=" ")
print_alphabets()

#Print a multiplication table of a given user inputed number.

def multiplication_table(number):
  for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number: "))
multiplication_table(number)
#Count no. of alphabets and no. of digits in any given user inputed string.

def count_alpha_digits(input_string):
    alpha_count = 0
    digit_count = 0
    for char in input_string:
        if char.isalpha():
            alpha_count += 1
        elif char.isdigit():
            digit_count += 1
    return alpha_count, digit_count

input_string = input("Enter a string: ")
alpha_count, digit_count = count_alpha_digits(input_string)
print("Number of alphabets:", alpha_count)
print("Number of digits:", digit_count)
#Check whether a user inputted number is prime, is perfect, is Armstrong, is palindrome, is automorphic
def is_prime(n):
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def is_perfect(n):
  sum_div = 1
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      sum_div += i + n//i
  return sum_div == n

def is_armstrong(n):
  num_str = str(n)
  num_digits = len(num_str)
  sum_digits = sum(int(digit)**num_digits for digit in num_str)
  return sum_digits == n

def is_palindrome(n):
  return str(n) == str(n)[::-1]

def is_automorphic(n):
  square = n**2
  return str(square).endswith(str(n))

number = int(input("Enter a number: "))

print(f"{number} is prime: {is_prime(number)}")
print(f"{number} is perfect: {is_perfect(number)}")
print(f"{number} is Armstrong: {is_armstrong(number)}")
print(f"{number} is palindrome: {is_palindrome(number)}")
print(f"{number} is automorphic: {is_automorphic(number)}")
# Generate all Pythagorean Triplets with side length <= 30.

def generate_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):
            c_squared = a**2 + b**2
            c = int(c_squared**0.5)
            if c**2 == c_squared and c <= limit:
                triplets.append((a, b, c))
    return triplets

limit = 30
triplets = generate_pythagorean_triplets(limit)
print(triplets)
#Print nCr and nPr with user inputed n and r

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

def permutations(n, r):
    return factorial(n) // factorial(n-r)

n = int(input("Enter n: "))
r = int(input("Enter r: "))

print("nCr =", combinations(n, r))
print("nPr =", permutations(n, r))
#Print factorial of a user inputed number

def factorial1(n):
    if n == 0:
        return 1
    else:
        return n * factorial1(n-1)

number = int(input("Enter a number: "))
print("Factorial of", number, "is", factorial1(number))
#Print N natural nos. in reverse.

n = int(input("Enter the value of N: "))

for i in range(n, 0, -1):
  print(i)
  # Generate N numbers of Fibonacci series.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        list_fib = [0, 1]
        while len(list_fib) < n:
            next_fib = list_fib[-1] + list_fib[-2]
            list_fib.append(next_fib)
        return list_fib

n = int(input("Enter the number of Fibonacci numbers to generate: "))
print(fibonacci(n))
# Calculate sin(x); x is a radian value. with series expansion

def sin_x(x, n_terms=10):
    sin_val = 0
    for i in range(n_terms):
        term = ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1)
        sin_val += term
    return sin_val

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x = float(input("Enter the radian value of x: "))
result = sin_x(x)
print(f"sin({x}) = {result}")