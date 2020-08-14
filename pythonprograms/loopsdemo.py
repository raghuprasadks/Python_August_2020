# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 20:12:59 2020

@author: lenovo
"""

'''
while
'''

'''
1. print 1 to 10
'''
start = 1
end = 10

while(start <= end):
    print(start)
    start = start +1
    
'''
1<10 - True
start = 1 + 1 = 2
2<10 - True
start = 2 + 1
'''

'''
2. Print 10 to 1
'''

start = 1
end = 10

while(end>=start):
    print(end)
    end = end-1
    
'''
3. Print 3's table 3 ... 30
'''

start = 3
end = 30

while(start <= end):
    print(start)
    start = start +3
    
'''
for loop
'''

'''
range is a number generator
'''
range(10) # 0 to 9    
range(1,11) # 1 to 10 ...step 1

'''
For loop print 1 to 10
'''
for i in range(1,11):
    print(i)
'''
prints from 10 to 1
'''
for i in range(10,0,-1):
    print(i)
'''
print from 0 to 9
'''
for i in range(10):
    print(i)
    
'''
print 2 's table
'''
for i in range(2,21,2):
    print(i)
    
'''
print 20 to 2 
'''

for i in range(20,1,-2):
    print(i)
    
'''
print 5's table '

5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
...
5 X 10 =50

'''

for i in range (5,51,5):
    print(i)
    
    
for i in range (1,11):
    print('5 X ',i,'=', 5*i)
    
counter = 1
for i in range (5,51,5):
    print('5 X ',counter,' = ',i)
    counter = counter +1
    
for i in range (10,0,-1):
    print('5 X ',i,'=', 5*i)
        

for i in range(10,0,-1):
    print ('6 x',i,'=',6*i)











