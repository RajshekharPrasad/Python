x1=int(input("x1"))
x2=int(input("x2"))
x3=int(input("x3"))
y1=int(input("y1"))
y2=int(input("y2"))
y3=int(input("y3"))
             
n1=x1-x2
n2=y3-y2
n3=y1-y2
n4=x3-x2

i=((n3*n4)-(n1*n2))

if(i==0):
  print("points are collinear")
else:
  print("not")
