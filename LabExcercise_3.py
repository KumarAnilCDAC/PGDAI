# from excercise no. 3
"""
#Q.1
A=[10,20,30,40,50]
b=sum(A)
print('Sum of list is',b)
#Q.2
c=max(A)
print('Max number in this list is',c)
#Q.3
d=min(A)
print('Min number in this list is',d)

#Q.4
color_list=["Red","Green","White","Black"]
Y=color_list[0]
Z=color_list[-1]
print('First Colour is',Y,' and ''Last Colour is',Z)


 


#Q.5
a=input(" Type any word")
if len(a)>=3:
    if a[-3:]=='ing':
        print(a+'ly')
    elif a[-2:]=='ly':
        print(a+'ing')
    else:
        print('sting is too short')
        
     
#Q.6
a=int(input('Marks in 1st Subject:'))
b=int(input('Marks in 2nd Subject:'))
c=int(input('Marks in 3rd Subject:'))
d=int(input('Marks in 4th Subject:'))
e=int(input('Marks in 5th Subject:'))
#a=40
#b=40
#c=40
#d=40
#e=40
add=a+b+c+d+e
result=add/500
final=result*100
print(add)
print(result)
print(final)
if final>=60:
    print('Percentage above or equal to 60 is First Division:','And your percentage is',final)
elif final>=50 and final<=59:
    print('Percentage between 50 or equal to 59 is Second Division:','And your percentage is',final)
elif final>=40 or final<=49:
    print('Percentage between 40 or equal to 49 is Third Division:','And your percentage is',final)
else:
    print('Percentage below 40 is Third Division:','And your percentage is',final)


#Q.7
a=50
b=60
c=70
if a>b and b>c:
    print('a is greater than among given numbers',a)
elif b>a and b>c:
    print('b is greater than among given numbers',b)
else:
    print('c is greater than among given numbers',c)



#Q.9
a="NITIN"
if a[::-1]==a[:]:
    print('String is Palindrome:',a)
else:
    print('String is not Palindrome:',a)

#Q.10
a='Goodjob'
b=a.split()
b.sort()
g=sorted(a)
print(g)
#new fomula of Q#10
a1="Good work is the best domation to the world"
b1=a.split()
b1.sort()
print(b1)


#Q.11
L1=["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
L2=["h","i","j"]

L1[2][1][2].extend(L2)
print(L1)

#Q.12

list1 = [5, 10, 15, 20, 25, 50, 20]
list1.index(20)
list1.insert(3,200)
print(list1)
#list1[list1.index(20)]=200

#Q.8
a=int(input('Enter the year to know Leap year:'))
if a/4==0:
    if a/100!=0:
        print('It is a Leap Year:',a)
        if a/400==0:
            print('It is a Leap Year:',a)
    
        
else:
    print('It is not a Leap Year:',a)
"""        
    
#Q.8
#a=int(input('Enter the year to know Leap year:'))
a=1991
if a/4==0:
    print('ok')
#    if a/100!=0:
#        print('It is a Leap Year:',a)
#        if a/400==0:
#            print('It is a Leap Year:',a)
    
        
#else:
#    print('It is not a Leap Year:',a)
        

#Q.8
#a=int(input('Enter the year to know Leap year:'))
"""
a=2001
if a/4==0:
    print('ok')
elif a/100!=0:
    print('good ok leap year')
elif a/100==0:
    print('good ok not a leap year')
elif a/400==0:
    print('It is a Leap year')
else:
    print('not ok, It is not a Leap year')

a=2012
if a/4==0:
    print('it is a leap year')
elif a/4==0 or a/100!=0:
    print('good ok it is a leap year')
elif a/4==0 or a/100==0 or a/400==0:
    print('good ok another a leap year')
else:
    print('not ok, It is not a Leap year')





a=2000
if a/4==0 and a/100!=0:
    print('good ok it is a leap year')
    if a/4==0 and a/100==0 and a/400==0:
        print('good ok another a leap year')
else:
    print('not ok, It is not a Leap year')
#it's working fine
a=2008
if a%4==0:
    print('It is a Leap Year.' )
elif a%4==0 and a%100!=0:
    print('good ok it is a leap year')
elif a%4==0 and a%100==0 and a%400==0:
        print('good ok another a leap year')
else:
    print('not ok, It is not a Leap year')

"""













