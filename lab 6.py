# Question 1: Find the number of boys (stored as tuples) and girls in a list.
def count_boys_girls():
    people = [("John",), "Emma", "Sophia", ("Michael", "Chris"), "Olivia"]
    boys = sum(len(person) for person in people if isinstance(person, tuple))
    girls = len(people) - sum(1 for person in people if isinstance(person, tuple))
    print("Number of boys:", boys)
    print("Number of girls:", girls)

count_boys_girls()
# Question 2: Create separate lists for roll numbers, names, and ages from a list of student tuples.
def separate_student_details():
    students = [(1, "Alice", 20), (2, "Bob", 21), (3, "Charlie", 22)]
    roll_numbers = [s[0] for s in students]
    names = [s[1] for s in students]
    ages = [s[2] for s in students]
    print("Roll Numbers:", roll_numbers)
    print("Names:", names)
    print("Ages:", ages)

separate_student_details()
# Question 3: Find the number of days between two dates represented as tuples (d, m, y).
from datetime import date

def days_between_dates():
    d1 = tuple(map(int, input("Enter first date (dd mm yyyy): ").split()))
    d2 = tuple(map(int, input("Enter second date (dd mm yyyy): ").split()))
    date1 = date(d1[2], d1[1], d1[0])
    date2 = date(d2[2], d2[1], d2[0])
    print("Number of days between dates:", abs((date2 - date1).days))

days_between_dates()
# Question 4: Create and sort a list of food item-price tuples in descending order by price.
def sort_food_items():
    food_items = [("Burger", 50), ("Pizza", 200), ("Pasta", 150), ("Sandwich", 100)]
    sorted_items = sorted(food_items, key=lambda x: x[1], reverse=True)
    print("Sorted Food Items by Price:", sorted_items)

sort_food_items()
# Question 5: Remove empty tuples from a list of tuples.
def remove_empty_tuples():
    tuples_list = [("Apple", 10), (), ("Banana", 20), (), ("Grapes", 30)]
    filtered_list = [t for t in tuples_list if t]
    print("List after removing empty tuples:", filtered_list)

remove_empty_tuples()
# Question 6: Modify an element of a tuple (since tuples are immutable, create a new tuple).
def modify_tuple():
    sample_tuple = (10, 20, 30, 40)
    index = int(input("Enter index to modify (0-3): "))
    new_value = int(input("Enter new value: "))
    modified_tuple = sample_tuple[:index] + (new_value,) + sample_tuple[index+1:]
    print("Modified Tuple:", modified_tuple)

modify_tuple()
# Question 7: Delete an element of a tuple by converting it to a list and back.
def delete_tuple_element():
    sample_tuple = (10, 20, 30, 40)
    index = int(input("Enter index to delete (0-3): "))
    temp_list = list(sample_tuple)
    del temp_list[index]
    new_tuple = tuple(temp_list)
    print("Tuple after deletion:", new_tuple)

delete_tuple_element()