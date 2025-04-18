# Write a program to create 3 dictionaries and concatenate them to create fourth
def concdict():
  dict1 = {'a': 1, 'b': 2}
  dict2 = {'c': 3, 'd': 4}
  dict3 = {'e': 5, 'f': 6}
  dict4 = dict1.copy()
  dict4.update(dict2)
  dict4.update(dict3)
  print(dict4)
concdict()
#Write a program to check whether a dictionary is empty or not
def empdict():
  a1 = {1:'S',2:'A',3:'U',4:'M',5:'Y',6:'A'}
  if not bool(a1):
    print("Dictionary is empty")
  else:
    print("Dictionary is not empty")
empdict()
#Create a dictionary with department no, employee roll no., and salary. Find out department wise min and max of salary

def deptsal():
  dict1 = {'a': [[1, 20000], [2, 40000], [3, 10000], [4, 14000]],
           'b': [[1, 21000], [2, 12000], [3, 15000], [4, 50000]],
           'c': [[1, 2000], [2, 40000], [3, 13000], [4, 17000]],
           'd': [[1, 37000], [2, 24000], [3, 19000], [4, 41000]]}

  for dept, employees in dict1.items():
    salaries = [emp[1] for emp in employees]
    min_salary = min(salaries)
    max_salary = max(salaries)
    total_salary= sum(salaries)
    print(f"Department {dept}: Min Salary = {min_salary}, Max Salary = {max_salary},Total Salary = {total_salary}")
deptsal()
#Create a dictionary with department no, employee roll no., and salary. Find out department wise min and max of salary

def deptsal():
  dict1 = {'a': [[1, 20000], [2, 40000], [3, 10000], [4, 14000]],
           'b': [[1, 21000], [2, 12000], [3, 15000], [4, 50000]],
           'c': [[1, 2000], [2, 40000], [3, 13000], [4, 17000]],
           'd': [[1, 37000], [2, 24000], [3, 19000], [4, 41000]]}

  for dept, employees in dict1.items():
    salaries = [emp[1] for emp in employees]
    dept_data={'Department' :dept,
              'min_salary'  : min(salaries),
              'max_salary'  : max(salaries),
              'total_salary': sum(salaries)}
    print(dept_data)

deptsal()
#Write a program that reads a string from the keyboard and creates dictionary containing frequency of each character occuring in string

def frechar():
  str1=input("Enter a String :")
  freq={}
  for char in str1:
    if char in freq:
      freq[char]+=1
    else:
      freq[char]=1
  print(freq)
frechar()
#Create two dictionaries one containing grocery items and their prices and another containing grocery items and quantity purchased. By using the values from these two dictionariescompute the total bill

def compute_bill():
    prices = {"apple": 5, "banana": 10, "orange": 15, "milk": 20}
    quantities = {"apple": 2, "banana": 3, "orange": 1, "milk": 1}

    total_bill = 0
    for item, price in prices.items():
        if item in quantities:
            total_bill += price * quantities[item]

    print(f"Total bill amount is: {total_bill}")

compute_bill()