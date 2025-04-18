# 1) Print largest and smallest values out of two.
def largest_smallest_of_two(a, b):
    return max(a, b), min(a, b)


largest_smallest_of_two(5, 10)
# 2) Print largest and smallest values out of three.
def largest_smallest_of_three(a, b, c):
    return max(a, b, c), min(a, b, c)


largest_smallest_of_three(5, 10, 3)
# 3) Check whether a given number is odd or even.
def is_odd_or_even(n):
    return 'Even' if n % 2 == 0 else 'Odd'


is_odd_or_even(7)
# 4) Check whether a given number is divisible by 10 or not.
def is_divisible_by_10(n):
    return n % 10 == 0


is_divisible_by_10(50)
# 5) Accept age of a person. If age is less than 18, print Minor otherwise Major.
def check_age_category(age):
    return 'Minor' if age < 18 else 'Major'


check_age_category(16)	
# 6) Accept a number from the user and print the number of digits in it.
def count_digits(n):
    return len(str(abs(n)))


count_digits(12345)

# 6 Accept input from the user
number = input("Enter a number: ")

# Calculate and print the number of digits
num_digits = len(number)
print(f"The number of digits in {number} is {num_digits}.")
# Accept input for the year
year = int(input("Enter a year: "))

#7 Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")





# 8) Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard.
def is_valid_triangle(a, b, c):
    return a + b + c == 180


is_valid_triangle(60, 60, 60)

# 9) Print absolute value of a given number.
def absolute_value(n):
    return abs(n)


absolute_value(-25)

# 10) Given the length and breadth of a rectangle, check if the area is greater than its perimeter.
def is_area_greater(length, breadth):
    return (length * breadth) > (2 * (length + breadth))


is_area_greater(10, 5)

# 11) Check if three points (x1,y1), (x2,y2), and (x3,y3) fall on the same straight line.
def are_collinear(x1, y1, x2, y2, x3, y3):
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)


are_collinear(1, 2, 2, 3, 3, 4)
# 12) Determine whether a point lies inside, on, or outside a circle given its center and radius.
import math

def point_circle_relation(cx, cy, r, px, py):
    distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
    if distance < r:
        return 'Inside'
    elif distance == r:
        return 'On'
    else:
        return 'Outside'


point_circle_relation(0, 0, 5, 3, 4)
# 13) Convert number 0 to 19 to its equivalent words.
def number_to_words(n):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
             'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
             'eighteen', 'nineteen']
    return words[n] if 0 <= n < 20 else 'Out of range'

number_to_words(10)
# 14) Accept marks of three subjects, print total and average, determine pass/fail, and assign grades.
def student_result(m1, m2, m3):
    total = m1 + m2 + m3
    avg = total / 3
    if m1 <= 39 or m2 <= 39 or m3 <= 39:
        return f'Fail - Total: {total}, Average: {avg:.2f}'

    grades = [(90, 'O'), (80, 'A+'), (70, 'A'), (60, 'B+'), (50, 'B'), (45, 'C'), (40, 'P'), (0, 'F')]
    grade = next(g for min_marks, g in grades if avg >= min_marks)
    return f'Pass - Total: {total}, Average: {avg:.2f}, Grade: {grade}'


student_result(85, 75, 65)
