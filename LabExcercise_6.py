#Lab 6
# Q.1
"""
a=open(r'D:\PythonWorkSept\pythonOct21\SampleCodes\excercise6file.txt',mode='r')
print(a.read())
print(a.close())

a=open(r'D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\excercise6file.txt',mode='r')
print(a.read())
a.close()


# By calling from same directory path and read mode
a=open('excercise6file.txt')
print(a.read())
a.close()

"""
# Q.2 A
"""
def countlines():
    #a=open(r'D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\excercise6file.txt',mode='r')
    a=open('excercise6file.txt',mode='r')
    #print(len(a.readlines()))
    print('The no. of lines in the file are =',len(a.readlines()))
    a.close()
# enable countlines for question no. 5 of lab 6
#countlines()

"""
"""
if (__name__=="__main__"):
    print('Original countlines file is open')
else:
    print('File is being imported')
"""
"""
# Q.2 B
def countchr():
    #a=open(r'D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\excercise6file.txt',mode='r')
    a=open('excercise6file.txt',mode='r')
    #print(len(a.read()))
    print('The total no. of Words in the file are =',len(a.read()))
    a.close()
# enable countchr for question no. 5 of lab 6
#countchr()
"""
"""
if (__name__=="__main__"):
    print('Original countchr file is open')
else:
    print('File is being imported')
"""

"""
# Q.2 C
def test():
    countlines()
    countchr()
#test()   

if (__name__=="__main__"):
    pass
    #test()
else:
    print('File is being imported')

"""
# Q.3
"""
"""
"""
#1st method
from mymod import countlines
#print(countlines())

#2nd method
from mymod import *


from mymod import test
"""
"""
#import mymod
from mymod import*
"""
"""
from mymod import countlines
from mymod import countchr
from mymod import test
"""
"""
Shell tested
==== RESTART: D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\Lab6_Q3.py ====
File is being imported
from mymod import countlines
countlines()
The no. of lines in the file are = 2
countchr()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    countchr()
NameError: name 'countchr' is not defined
from mymod import countchr()
SyntaxError: invalid syntax
from mymod import countchr
countchr()
The total no. of Words in the file are = 59
test()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    test()
NameError: name 'test' is not defined
from mymod import test
test()
The no. of lines in the file are = 2
The total no. of Words in the file are = 59

==== RESTART: D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\Lab6_Q3.py ====
File is being imported
test()
The no. of lines in the file are = 2
The total no. of Words in the file are = 59
countlines()
The no. of lines in the file are = 2
countchr()
The total no. of Words in the file are = 59
from mymod.countchr()
SyntaxError: invalid syntax
import mymod
test()
The no. of lines in the file are = 2
The total no. of Words in the file are = 59
"""
# Q.4

"""
#1st method
from mymod import countlines
#print(countlines())

#2nd method
from mymod import *


from mymod import test

from mymod import test

#Q.4
import mymod
#mymod.test()


#from mymod import *
import mymod
"""
"""
import Lab6_Q3
"""
"""
Shell tested

==== RESTART: D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\Lab6_Q4.py ====
File is being imported
Lab6_Q3.countchr()
The total no. of Words in the file are = 59
Lab6_Q3.countchr()
The total no. of Words in the file are = 59
Lab6_Q3.count()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    Lab6_Q3.count()
AttributeError: module 'Lab6_Q3' has no attribute 'count'
Lab6_Q3.test()
The no. of lines in the file are = 2
The total no. of Words in the file are = 59
countlines()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    countlines()
NameError: name 'countlines' is not defined
import mymod
countlines()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    countlines()
NameError: name 'countlines' is not defined
mymod.countlines()
The no. of lines in the file are = 2
mymod.countchr()
The total no. of Words in the file are = 59
mymod.test()
The no. of lines in the file are = 2
The total no. of Words in the file are = 59

"""
#Q.5
"""
# From 1st method
#import mymod
# From 2nd method
#from mymod import* 
#from mymod import countlines
#from mymod import countchr
#from mymod import test

import Lab6_Q4
"""
"""
Shell tested

==== RESTART: D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\myclient.py ===
File is being imported
Lab6_Q4.Lab6_Q3.countchr()
The total no. of Words in the file are = 59
Lab6_Q4.Lab6_Q3.countlines()
The no. of lines in the file are = 2
Lab6_Q4.Lab6_Q3.test()
The no. of lines in the file are = 2
The total no. of Words in the file are = 59
import mymod
test()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    test()
NameError: name 'test' is not defined
mymod.test()
The no. of lines in the file are = 2
The total no. of Words in the file are = 59

"""
#Q.6
"""
import myclient
"""
"""
# In Shell tested
= RESTART: D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\Lab6_Q7_changer.py .py
import mypkg
mypkg.myclient
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    mypkg.myclient
AttributeError: module 'mypkg' has no attribute 'myclient'
mypkg.myclient()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    mypkg.myclient()
AttributeError: module 'mypkg' has no attribute 'myclient'
from mypkg
SyntaxError: incomplete input
import mypkg
mypkg.__path__
['D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg']
mypkg.__cached__
'D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg\\__pycache__\\__init__.cpython-311.pyc'
mypkg.__doc__
mypkg.__file__
'D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg\\__init__.py'
mypkg.__loader__
<_frozen_importlib_external.SourceFileLoader object at 0x000002A2C1776FD0>
mypkg.__name__
'mypkg'
mypkg.__spec__
ModuleSpec(name='mypkg', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000002A2C1776FD0>, origin='D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg\\__init__.py', submodule_search_locations=['D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg'])
import mymod
File is being imported
mymod.countlines()
The no. of lines in the file are = 2
import Lab6_Q4
lab6_Q4.countlines
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    lab6_Q4.countlines
NameError: name 'lab6_Q4' is not defined. Did you mean: 'Lab6_Q4'?
import myclient
myclient.Lab6_Q4.Lab6_Q3.countchr()
The total no. of Words in the file are = 59

"""
#Q.7


"""
import Addition10

#from Addition10 import*
Addition10.add(10,20)

import importlib
importlib.reload(Addition10)

Addition10.mul(10,20)
"""
"""
import mypkg
"""

"""
Shell tested
= RESTART: D:\PythonWorkSept\pythonOct21\SampleCodes\mymod.py\Lab6_Q7_changer.py .py
import mypkg
mypkg.myclient
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    mypkg.myclient
AttributeError: module 'mypkg' has no attribute 'myclient'
mypkg.myclient()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    mypkg.myclient()
AttributeError: module 'mypkg' has no attribute 'myclient'
from mypkg
SyntaxError: incomplete input
import mypkg
mypkg.__path__
['D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg']
mypkg.__cached__
'D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg\\__pycache__\\__init__.cpython-311.pyc'
mypkg.__doc__
mypkg.__file__
'D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg\\__init__.py'
mypkg.__loader__
<_frozen_importlib_external.SourceFileLoader object at 0x000002A2C1776FD0>
mypkg.__name__
'mypkg'
mypkg.__spec__
ModuleSpec(name='mypkg', loader=<_frozen_importlib_external.SourceFileLoader object at 0x000002A2C1776FD0>, origin='D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg\\__init__.py', submodule_search_locations=['D:\\PythonWorkSept\\pythonOct21\\SampleCodes\\mymod.py\\mypkg'])
import mymod
File is being imported
mymod.countlines()
The no. of lines in the file are = 2
import Lab6_Q4
lab6_Q4.countlines
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    lab6_Q4.countlines
NameError: name 'lab6_Q4' is not defined. Did you mean: 'Lab6_Q4'?
import myclient
myclient.Lab6_Q4.Lab6_Q3.countchr()
The total no. of Words in the file are = 59
"""


