"""
#Q.1
a=float(input("Enter the raduis:"))
import math
b=math.pi
c=b*a*a
print("The radius area is",c)
#print("The radius area is",b)

#Q.2
a=float(input("Enter the city temp. in Farehneight:"))
b=(a-32)*5/9
print("The temp. in degree centigrade area is ",b)

#Q.3
a=float(input("Enter the First Number:"))
b=float(input("Enter the Second Number:"))
c=a+b
d=a-b
e=a*b
f=a/b
print("The addition of given number is ",c)
print("The subtraction of given number is ",d)
print("The multiplication of given number is ",e)
print("The division of given number is ",f)

#Q.4
a=float(input("Enter the Number to get the square:"))
import math
b=math.sqrt(a)
print("The square rot of {0} is ={1}".format(a,b))


#Q.5
a=float(input("Enter the First cofficient Number:"))
b=float(input("Enter the Second cofficient Number:"))
c=float(input("Enter the Third cofficient Number:"))
import cmath
z=b**2-4*a*c
#sol1=(-b+sqrt(b**2-4*a*c))/2*a
#sol2=(-b-sqrt(b**2-4*a*c))/2*a
sol1=(-b+cmath.sqrt(z))/2*a
sol2=(-b-cmath.sqrt(z))/2*a
print("The soluction of 1st Quardatic Equation is:",sol1)
print("The soluction of 2nd Quardatic Equation is:",sol2)

#Q.6
a=float(input("Enter the First Traingle Area:"))
b=float(input("Enter the Second Traingle Area:"))
c=float(input("Enter the Third Traingle Area:"))
s=(a+b+c)/2
A=(s*(s-a)*(s-b)*(s-c))**0.5
print("The Area of triangle  %0.2f :"%A)


#Q.7
a=int(input("Enter the Five Digit Number "))
sum=0
A=a%10
sum=sum+A
print(sum)
B=a//10
print(B)
C=B%10
sum=sum+C
print(sum)
E=B//10
print(E)
F=E%10
sum=sum+F
print(sum)
G=E//10
print(G)
H=G%10
sum=sum+H
print(sum)
I=G//10
print(I)
sum=sum+I
print("Sum of given Number is :",sum)



#Q.8
a=("Twinkle, twinkle, little star,
             How I wonder what you are!
                     up above the world so high,
                     Like a diamond in the sky.
     Twinkle, twinkle, little star,
             How I wonder what you are")
print("Your Typed string is this:",a)

#Q.9
a=str(input("Enter your Name:"))
b=float(input("Enter the Age:"))
c=(input("Enter the Address:"))
print("Person Name is {0}, and Age is {1} years, and the Address is {2} ".format(a,b,c))
"""

