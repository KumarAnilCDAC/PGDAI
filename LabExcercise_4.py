#Q.1
"""
sum=0
for i in range(21):
    if i%2!=0:
        sum=sum+i
        print(sum)

a=[i for i in range(20) if i%2!=0]
print(sum(a))


print([i for i in range(20) if i%2!=0])
print([(i) for i in range(20) if i%2!=0])
print(sum([(i) for i in range(20) if i%2!=0]))

c=[sum(int(i) for i in range(1,20,2))]
print(c)

#Q.1
print(sum([i for i in range(0,20) if i%2!=0]))
print(sum([i for i in range(0,20) if i%2!=0]))

#Q.2
sum=0
for i in range(100,200):
    sum=sum+i
    print(sum)


print(sum([a for a in range(100,200)]))

#Q.2
print(sum(i for i in range(100,200)))
print(sum(i for i in range(200) if i>=100 and i<=200))


#Q.2
c=[sum(int(i) for i in range(101,200))]
print(c)

add=0
for d in range(101,200):
    add+=d
    print(add)



sum=0
for i in range(20):
    if(i%2!=0):
       sum+=i
       print(sum)
    

#    print('The sum of from 1 to {20}=',(i,sum))

#for a in range(0,20) if a%2!==0:
#    print(a)
    
b=[sum(int(a)) for a in range(0,20) if a%2!=0]
print(b)




   
#Q.3
f=[sum(int(e)**2 for e in range(0,21,2))]   
print(f)

sum=0
for i in range(0,21):
    
    tum=i**i
#    print(sum)
    print(tum)

Add=0
for i in range(0,20):
    if i%2!=0:
        Add=Add+i
        print(Add)
#Q.3
sum=0
for i in range(20):
#    sum=sum+i*i
    c=i*i
    print(c)
#    print(sum)



#Q.3
#print(sum(i*i for i in range (0,21) if i%2==0))
print([i for i in range (2,21) if i%2==0])

print(sum([(x*x) for x in range(11) if x%2!=0]))


L1=0
for i in range(0,21):
    if i%2==0:
        x=i*i
        L1=L1+x
    else:
        continue
print("Sum of square for first ten even natural number ",L1)

i=1
while(i<=10):
    print(2*i)
    i=i+1
#    print(i)

#Q.4
for i in range(65,91):
    print(i,'=',chr(i))

#Q.5
for i in range(48,58):
    print(i,'=',chr(i))

#Sample try question Q.0
for i in range(0,501):
    print(i,'=',chr(i))

#Q.4
for i in range(65,91):
    print(i,'=',chr(i))

#Q.6
for i in range(97,123):
    print(i,'=',chr(i))

#Q.7
L1=[100,200,300,400,500]
L2=L1[::-1]
print(L2)
L1.reverse()
print(L1)

L4=L1.reverse()
print(L4)
L5=sorted(L1)
print(L5)
L6=(reversed(L1)
print(L6)

#Q.8
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dic1.update(dic2)
print(dic1)
dic1.update(dic3)
print(dic1)


#Q.9
dic1={0:10, 1:20}
dic1[2]=30
print(dic1)

#Q.10
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
a=color_list_1
b=color_list_2
c=a-b
print(c)
print(type(c))
#print(a)
#print(b)
 
#Q.11
List1 = [1, 2, 3, 4, 5, 6, 7]
print([i*i for i in (List1)])
print([i*i for i in (List1) if i%2==0])
print([i*i for i in (List1) if i%2!=0])
print(sum([i*i for i in (List1) if i%2==0]))
print(sum([i*i for i in (List1) if i%2!=0]))

#Q.13
Dict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(Dict['class'])
print(Dict['class']['student'])
print(Dict['class']['student']['name'])
print(Dict['class']['student']['marks'])
print(Dict['class']['student']['marks']['history'])
D={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(D)
print(D['class']['student']['marks']['history'])

e={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
g=e['class']['student']['marks']['history']
print(g)

Dict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}

a=(Dict.get("class"))
print(a)
b=(a.get("student"))
print(b)
#c=(b.get("name"))
#print(c)
d=(b.get("marks"))
print(d)
e=(d.get("physics"))
print(e)
f=(d.get("history"))
print(f)

Dict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
a=Dict['class']
print(a)
b=a['student']
print(b)
#c=b[name]
#print(c)
d=b['marks']
print(d)
e=d['physics']
print(e)
f=d['history']
print(f)



Dict = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
a=Dict["class"]
print(a)
b=a["student"]
print(b)
#c=b["name"]
#print(c)
d=b["marks"]
print(d)
e=d["physics"]
print(e)
f=d["history"]
print(f)

"""

"""
#Q.12
a=input('Enter the string:')
b=('a','e','i','o','u')
cnt=0
for i in (a):
    if i=='a' or 'e' or 'i' or 'o' 'u':
        cnt=cnt+1
        print(cnt)
      
#Q.14
import string
a=string.punctuation
print(a)
b=input('Enter the string with above punctuation')
for i in (b):
    if a in b:
        c=b.remove(a)
        print(c)


#Q.15
for i in range(1,4):
    for j in range(i,0+1,-1):
        print(j,end =" ")
    print(i)

for i in range(1,4):
    for j in range(i):
        print(j, end =" ")
    print(i)
#    print(i)

#Q.14
import string
a=string.punctuation
print(a)
b=input('Enter the string with above punctuation:')
cnt=""
for i in b:
    if i not in a:
        cnt=cnt+i
print(cnt)

#a=['10','20','30','40','50']
#b=['100','200','300','40','50']
a=['a','b','c','d','e']
b=['f','g','h','a','e']
chk=''
for i in a:
    if i not in b:
#        chk=chk+i
        chk+=i
print(chk)
"""
"""
#Q.12
a=input('Enter the string here:')
b=['a','e','i','o','u']
cnt1=''
cnt2=''
cnt3=''
cnt4=''
cnt5=''
for i in a:
    if a==b[0]:
        cnt1+=1
print(cnt1)


for i in range(0,4):
    for j in range(i+1):
        print(j,end=" ")
    print()
"""
"""
# NOt correct with numbers
#Q.16
for i in range(0,5):
    for j in range(i):
        print('*',end=" ")
    print()

#Q.15
for i in range(1,4):
    for j in range(i,0+1,-1):
        print(j,end =" ")
    print(i)


for i in range(1,4):
    for j in range(i):
        print(j, end =" ")
    print(i)
#    print(i)


sm=0
for i in range(2,21,2):
    sm=sm+(i*i)
    #print(i)
print('Sum value:',sm)
       

for i in range(1,4):
    for j in range(i,0+1,-1):
        print(j,end =" ")
    print(i)
1
2 2
3 2 3

for i in range(1,4):
    for j in range(i,0+1,-1):
        print(j,end =" ")
    print()
2 
3 2
for i in range(10,0,-1):
    print(i,end = ' ')


#Q.15
for i in range(1,4):
    for j in range(i,0,-1):
        print(j,end =" ")
    print()

print('#############')
for a in range(3,0,-1):
    print(a,end = ' ')

#Q.16
for i in range(6):
    for j in range(i+1):
        print('*',end = ' ')
    print()

#Q.17
for i in range(4):
    for j in range(i+1):
        print('*',end = ' ')
    print()

for i in range(3,0,-1):
    for j in range(i):
        print('*',end = ' ')
    print()

#Q.17
for i in range(4):
    for j in range(i+1):
        print(i,end = ' ')
    print()

for i in range(3,0,-1):
    for j in range(i):
        print(i,end = ' ')
    print()

#Q.18
for i in range(1,11):
    print('|',end ='\n')
    for j in range(11):
        print(i*j,end = '\t')
    print()
"""
#Q.12
s=('Anil Kumar our student')
print('The vowel a comes',s.count('a',0,len(s)),'Times')
print('The vowel a comes',s.count('e',0,len(s)),'Times')
print('The vowel a comes',s.count('i',0,len(s)),'Times')
print('The vowel a comes',s.count('o',0,len(s)),'Times')
print('The vowel a comes',s.count('u',0,len(s)),'Times')

