#Q.2
"""
a=int(input('Enter the number:'))
b=int(input('Enter the power number:'))
c=(map(lambda a,b: a*b,a,b))
print(c)

x=int(input('Enter the number :'))
y=lambda x:x*2
print(y(x))

uip=[int(i) for i in input('Enter the input:').split()]
print(uip)
y=list(map(lambda x:x**2,uip))
print(y)
"""
"""
# NOT working
a=int(input('Enter the number:'))
b=int(input('Enter the power number:'))
c=list(map(lambda a,b: a*b,a,b))
#c=list(map(lambda a,b: a*b,a,b))
print(c(a,b))

# NOT working
x=int(input('Enter the number :').split)('')
y=lambda x:x*2
print(y(x))

#Q.3
a=[100,200,300,400,500]
b=[30]
c=list(map(lambda a,b:a/b,a,b))
print(c)

a=[100,200,300,400,500]
b=[30,30,30,30,30]
c=list(map(lambda a,b:a/b,a,b))
print(c)

numbers=[1,2,3,4,5]
t1=(6,7,8,9,10)
result=list(map(lambda x,y:x*y,t1,t1))
print(result)

numbers=[6,7,8,9,10]
t1=[1,2,3,4,5]
result=list(map(lambda x,y:x//y,numbers,t1))
print(result)

#LAB#4 Q.17
#a=int(input('Enter the number:'))
for i in range(1,11):
    print('\t',i,end='')
print('\n+++++++++++++++++++++++++++++++++')
for i in range(1,11):
    if i<10:
        print(' ',end='')
    print(i,'|',end='')
    for j in range(1,11):
        print(i*j,end='\t')
    print()


    
       
a=int(input('Enter the number:'))
b=list(map(lambda c:c**2,range(a)))
print(b)

#Q.1
a=int(input('Enter the number:'))
b=0
c=1
for i in range(0,a):
    d=b+c
    print('the no is:',c)
    b=c
    c=d
#print()

 
#Q.1
A=int(input('Enter the number for Fibanacii sequence:'))
a=0
b=1
c=0
while c<=A:
    print('Fibanacii sequence is :',c)
    a=b
    b=c
    c=a+b
#Q.3
a=[10,20,30,40,50]
result=list(map(lambda x:x/13,a))
print(result)

OR
a=[10,20,30,40,50,13]
result=list(filter(lambda x:(x%13==0),a))
print(result)
"""
"""
#Q.4
A=int(input('Enter the number for Fibanacii sequence:'))
a=2
b=3
c=a+b
print(c)

#Q.6
A=int(input('Enter the no. to conert in to binary number:'))
def con(A):
    if A>0:
        con(A//2)
        print(A%2,end='')
con(A)
"""
#Q.5
x=int(input('Enter the number up to which sum of natural numbers you want:'))
def s1(x):
    if x==0:
        return 0
    else:
        return x+s1(x-1)
print('The Sum of Natural Numbers are :',s1(x))
print()
