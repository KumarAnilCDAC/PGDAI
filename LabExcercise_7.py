# Q.1
"""
a=open('Exer7File.txt',mode='r')
rows=4
for i in range(rows):
    #final=a.readlines(4)
    final=a.readline()
    print(final)

#Q.2
# Append Function
a=open('Exer7File.txt',mode='a+')
a.write('is everthing fine')
#a.writelines('is everthing fine')
a.seek(0)
print(a.read())
a.close()

#OR
x=[str(i) for i in input('Enter the number of lines=:').split()]
a=open('Exer7File.txt',mode='a+')
a.writelines(x)
a.seek(0)
print(a.read())
a.close()

#Q.3
a=open('Exer7File.txt')
b=a.readline()
#print(b)

L=[]
for i in range(0,len(b)):
    c=L.append(b[i])
    i+=1
print(L)
a.close()
"""
"""
#Q.4
#NOT Working
a=open('Exer7File.txt')
b=a.readlines()
#c=b[::-1]
for i in range(0,len(b)):
    k=b[i][::-1]
print(k)
a.close()

#Q.4
a=open('Exer7File.txt')
b=a.readlines()
#print(b)
print(b[::-1])
a.close()

a=open('Exer7File.txt')
b=a.readlines()
c=b[::-1]
for i in range(0,len(c)):
    print(c[i])
a.close()

#Q.5
a=open('Exer7File.txt',mode='a')
b=['One','Two','Three']
a.write('\n'+str(b))
a.close()

#Q.6
a=open('Exer7File.txt',mode='r')
b=a.read()
c=len(b)
#c=b.count(b)
print('NO. of characters:',c)
d=b.split()
e=len(d)
print('NO. of Words:',e)
a1=open('Exer7File.txt',mode='r')
b1=a1.readlines()
f=len(b1)
print('NO. of Lines:',f)
a.close()

#Q.7
import datetime
now=datetime.datetime.now()
print(now-datetime.timedelta(days=7))

#Q.8
import datetime
my_date=datetime.datetime(2020,12,18,11,0,0)
print(my_date + datetime.timedelta(days=7,hours=12))

#Q.9
import datetime
now=datetime.datetime.now()
count=0
while(count<10):
    print(now.strftime('%Y-%m-%d'))
    now=now+datetime.timedelta(days=1)
    count+=1

#Q.10
import datetime
my_date=datetime.datetime(2020,4,18)
my_date1=datetime.datetime(2020,12,18)
if my_date<my_date1:
    print('First Condition:',my_date1-my_date)
elif my_date<my_date1:
    print('Second Condition:',my_date-my_date1)
else:
    print('No Difference between Date')

#Q.11
import datetime
now=datetime.datetime.today()
print('Current Date and Time now:',now)
#print(now.strftime('Current Year in full:%Y \n Month of year in full:%B \n Weekday of the week:%a \n Day of week in full name:%d',))

#Q.12
import datetime
st= 'Jul 1 2016 2:43AM'
#formula '%Y-%m-%d %H:%M:%S'
data = datetime.datetime.strptime(st,'%b %d %Y %H:%M%p')
print(data)
"""
#Q.13
from datetime import datetime
date=input(2022/1/24)
#date=input('Enter date in Year/Month/Day format')
date1=datetime.strftime(date,'%Y/%m/%d')
print(date1)
totalday=date1.strftime('%j')
print('Day number of Year:',date1.year,'is',totalday)
