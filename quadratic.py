#quadratic formula
import math


a=int(input("enter the value of b:"))
b=int(input("enter the value of a:"))
c=int(input("enter the value of c:"))
x1=(b**2+math.sqrt(4*a*c))/2*a
x2=(b**2-math.sqrt(4*a*c))/2*a
print(x1,x2)
if(x1<0):
 print("x1 is imaginary root")
else:
  print("x2 is real root")



