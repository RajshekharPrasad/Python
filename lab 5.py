# Question 1: Create a list of 5 odd integers and 4 even integers, replace the third element of odd integers with a list of 4 even integers, flatten, sort, and print.
import random

def create_list():
    odd_numbers = [random.randint(1, 50) * 2 + 1 for _ in range(5)]
    even_numbers = [random.randint(1, 50) * 2 for _ in range(4)]
    print("Odd Numbers:", odd_numbers)
    print("Even Numbers:", even_numbers)
    odd_numbers[2] = even_numbers
    print("After Replacement:", odd_numbers)
    flattened = [num for sublist in odd_numbers for num in (sublist if isinstance(sublist, list) else [sublist])]
    print("Flattened List:", flattened)
    flattened.sort()
    print("Sorted List:", flattened)

create_list()
# Question 2: Generate 20 random integers, accept a number from the user, and print the positions of all occurrences.
def find_occurrences():
    numbers = [random.randint(1, 100) for _ in range(20)]
    print("Generated List:", numbers)
    num = int(input("Enter a number to find: "))
    positions = [i for i, val in enumerate(numbers) if val == num]
    print("Positions:", positions if positions else "Number not found")

find_occurrences()
# Question 3: Generate 50 random numbers in range 1-30 and remove duplicates.
def remove_duplicates():
    numbers = [random.randint(1, 30) for _ in range(50)]
    print("Original List:", numbers)
    unique_numbers = list(set(numbers))
    print("List without duplicates:", unique_numbers)

remove_duplicates()
# Question 4: Generate 30 random numbers and create separate lists for positive and negative numbers.
def separate_numbers():
    numbers = [random.randint(-50, 50) for _ in range(30)]
    print("Original List:", numbers)
    positive_numbers = [num for num in numbers if num > 0]
    negative_numbers = [num for num in numbers if num < 0]
    print("Positive Numbers:", positive_numbers)
    print("Negative Numbers:", negative_numbers)

separate_numbers()
# Question 5: Convert a list of 5 strings to uppercase.
def convert_to_uppercase():
    strings = ["hello", "world", "python", "programming", "lists"]
    uppercased = [s.upper() for s in strings]
    print("Uppercase Strings:", uppercased)

convert_to_uppercase()
# Question 6: Convert a list of Fahrenheit temperatures to Celsius.
def fahrenheit_to_celsius():
    fahrenheit = [32, 68, 104, 212]
    celsius = [(temp - 32) * 5/9 for temp in fahrenheit]
    print("Celsius Temperatures:", celsius)

fahrenheit_to_celsius()
# Question 7: Implement a menu-driven stack data structure.
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print("Pushed", item)

    def pop(self):
        if self.stack:
            print("Popped", self.stack.pop())
        else:
            print("Stack is empty")

    def display(self):
        print("Stack:", self.stack)
def stack_menu():
    s = Stack()
    while True:
        choice = input("Enter push, pop, display or exit: ")
        if choice == "push":
            s.push(int(input("Enter number: ")))
        elif choice == "pop":
            s.pop()
        elif choice == "display":
            s.display()
        elif choice == "exit":
            break

stack_menu()
# Question 8: Implement a menu-driven queue data structure.
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print("Enqueued", item)

    def dequeue(self):
        if self.queue:
            print("Dequeued", self.queue.pop(0))
        else:
            print("Queue is empty")

    def display(self):
        print("Queue:", self.queue)

def queue_menu():
    q = Queue()
    while True:
        choice = input("Enter enqueue, dequeue, display or exit: ")
        if choice == "enqueue":
            q.enqueue(int(input("Enter number: ")))
        elif choice == "dequeue":
            q.dequeue()
        elif choice == "display":
            q.display()
        elif choice == "exit":
            break

queue_menu()
# Question 9: Take two lists and create a third list with elements from the first list that are not in the second list.
def list_difference():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    result = [num for num in list1 if num not in list2]
    print("Difference List:", result)

list_difference()
