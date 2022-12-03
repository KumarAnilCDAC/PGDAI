"""

#a=(input("Enter the raduis:"))

#print("Creating sting with single and double quote",c)
#Q.9

s1=""""abc""xyz""""
Result=s2[:2]+s1[-1]
Result1=s1[:2]+s2[-1]
print(Result + Result1)


s1=""""abc""xyz""""
Result=s1[:2]+s1[-1]
Result1=s1[:2]+s2[-1]
print(Result + Result1)
"""
#Q.1
#a=""""GOOD"'Work'"""
a="I'm a good person"
print(a)
#Q.2
b='''I'm a good person'''
#b="""'GOOD'''Look''"""
print(b)
#Q.3
a='A'
print(type(ord(a)),ord(a))

#Q.4
c='RAM '
print(c*5)
#Q.5
a='-'*50
print(a*50)
#Q.6
a='good country'
print(a.upper())

#Q.7
a='Apple'
b='Orange'
c=a[:2]+b[-2:]
print(c)

#Q.8
a='restart'
A=a[0]
B=a[1:]
C=B.replace('r','$')
D=A+C
print(D)

#Q.9

#Q.9
"""
s1=""""abc""xyz""""
Result=s2[:2]+s1[-1]
Result1=s1[:2]+s2[-1]
print(Result + Result1)
"""
##Q.9
a='abc'
b='xyz'

c=a[0]+b[1:] +" "+ b[0]+a[1:]
print(c)
