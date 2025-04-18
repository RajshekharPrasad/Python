# object lab 12
#question 2
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_part, imag_part)

    def __truediv__(self, other):
        denom = other.real ** 2 + other.imag ** 2
        real_part = (self.real * other.real + self.imag * other.imag) / denom
        imag_part = (self.imag * other.real - self.real * other.imag) / denom
        return ComplexNumber(real_part, imag_part)

    def __repr__(self):
        return f"{self.real} + {self.imag}i"

# Example usage
a = ComplexNumber(4, 5)
b = ComplexNumber(2, 3)
print(a + b)  # ComplexNumber(6, 8)
print(a - b)  # ComplexNumber(2, 2)
print(a * b)  # ComplexNumber(7, 22)
print(a / b)  # ComplexNumber(1.6153846153846154, 0.07692307692307693)

#question 2 
class Matrix:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        result = [[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __mul__(self, other):
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

# Example usage
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(matrix1 + matrix2)  # Matrix sum
print(matrix1 * matrix2)  # Matrix multiplication
print(matrix1.transpose())  # Matrix transpose
#question 03
import math

class Solid:
    def __init__(self, solid_type, **dimensions):
        self.solid_type = solid_type
        self.dimensions = dimensions

    def surface_area(self):
        if self.solid_type == 'sphere':
            radius = self.dimensions['radius']
            return 4 * math.pi * radius ** 2
        elif self.solid_type == 'cube':
            side = self.dimensions['side']
            return 6 * side ** 2
        else:
            return None

    def volume(self):
        if self.solid_type == 'sphere':
            radius = self.dimensions['radius']
            return (4/3) * math.pi * radius ** 3
        elif self.solid_type == 'cube':
            side = self.dimensions['side']
            return side ** 3
        else:
            return None

# Example usage
sphere = Solid('sphere', radius=5)
cube = Solid('cube', side=3)

print(sphere.surface_area())  # 314.1592653589793
print(cube.volume())  # 27
 #question 04
 class RegularShape:
    def __init__(self, shape_type, **dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def perimeter(self):
        if self.shape_type == 'circle':
            radius = self.dimensions['radius']
            return 2 * math.pi * radius
        elif self.shape_type == 'square':
            side = self.dimensions['side']
            return 4 * side
        else:
            return None

    def area(self):
        if self.shape_type == 'circle':
            radius = self.dimensions['radius']
            return math.pi * radius ** 2
        elif self.shape_type == 'square':
            side = self.dimensions['side']
            return side ** 2
        else:
            return None

# Example usage
circle = RegularShape('circle', radius=4)
square = RegularShape('square', side=5)

print(circle.perimeter())  # 25.132741228718345
print(square.area())  # 25
# question 05
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) + \
                        (other.hours * 3600 + other.minutes * 60 + other.seconds)
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return Time(hours, minutes, seconds)

    def __repr__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Example usage
time1 = Time(2, 30, 45)
time2 = Time(1, 15, 30)

print(time1 + time2)  # 03:46:15

#question 06
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __eq__(self, other):
        return (self.day == other.day and self.month == other.month and self.year == other.year)

    def __repr__(self):
        return f"{self.day}/{self.month}/{self.year}"

# Example usage
date1 = Date(17, 4, 2025)
date2 = Date(17, 4, 2025)
date3 = Date(16, 4, 2025)

print(date1 == date2)  # True
print(date1 == date3)  # False
#question 7
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

# Example usage
weather = Weather(['temperature', 'humidity', 'wind_speed'])

print('temperature' in weather)  # True
print('rainfall' in weather)  # False
#question 8
class MyString:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        self.value += other
        return self

    def to_lower(self):
        return self.value.lower()

    def to_upper(self):
        return self.value.upper()

    def __repr__(self):
        return self.value

# Example usage
my_str = MyString("Hello")
my_str += " World"
print(my_str)  # "Hello World"
print(my_str.to_lower())  # "hello world"
print(my_str.to_upper())  # "HELLO WORLD"



