#Write a program that converts words present in a list into uppercase and stores them in a set
def setfunc():
  lst=['aaa','BBB','Ccc','cCC']
  lst2 = []
  for ele in lst:
    lst2.append(ele.upper())
  s1=set(lst2)
  print(s1)
setfunc()
#Write a program to create a set containing 10 random numbers in the range 15 to 45, Count how many of the numbers are less than 30. Delete all Numbers that are greater than 35
import random as r
def Nos():
  set1=set()
  while len(set1)<10:
      set1.add(r.randint(15,45))
  print("Original set:", set1)
  count = 0
  for num in set1:
    if num < 30:
      count += 1
  print("Numbers less than 30:", count)

  s2 = set()
  for num in set1:
    if num <= 35:
      s2.add(num)
  print("Set after removing numbers greater than 35:", s2)
Nos()
#Create an Empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.
def setfunc():
  s1=set()
  while len(s1)<5:
    s1.add(input('Enter a Name: '))
  print(s1)
  nm=input("Enter Name to Modify:")
  if nm in s1:
      newnm=input('Enter a Name: ')
      s1.remove(nm)
      s1.add(newnm)
  print("Removing two items")
  print(s1.pop(),"is removed")
  print(s1.pop(),"is removed")
  print("Modified Set:",s1)
setfunc()
#A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names begining with A and another with B
def setv():
    ab=set()
    A=set()
    B=set()
    while len(ab)!=5:
        ab.add(input("Enter Names starting with either A or B:"))
    for i in ab:
       if i[0]=='A' or  i[0]=='a':
           A.add(i)
       if i[0]=='B' or  i[0]=='b':
           B.add(i)
    print("A=",A,"B=",B)
setv()