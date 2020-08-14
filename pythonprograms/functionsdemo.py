# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:11:42 2020

@author: lenovo
"""
def greet():
    print('Welcome to Python class')

greet()

def greet(name):
    print(name,' welcome to python')
    
greet("Ravi")

greet("Ramya")

'''
calculator
n1 - parameter
n2 - parameter
def - defind
add - name of the function
'''

def add(n1,n2):
    result = n1+n2
    print('Result of addition ',result)
    
add(100,150)
    
'''
write function for
subtraction,multiplication,
division
'''

def subtract(n1,n2):
    result = n1-n2
    print('Result of subtraction ',result)
    
subtract(200,150)

def multiplication(n1,n2):
    result = n1*n2
    print('Result of multiplication ',result)
    
multiplication(20,15)

def division(n1,n2):
    result = n1/n2
    print('Result of division ',result)
    
division(30,15)

'''
write a function to check a given number
is odd or even
'''

def oddOrEven(n):
    if n%2 ==0 :
        print('even')
    else:
        print('odd')
        
oddOrEven(12)

num = int(input("Enter a number"))
oddOrEven(num)

'''
Write a function to 
find the simpleInterest
by passing three values
By getting user inputs

si=p*r*t/100
'''

def si(p,t,r):
    result = (p*t*r)/100
    print('simple intrest = ',result)
    
p = int(input('enter the principal amount'))
t = int(input('enter the time of deposit'))
r = int(input('enter the rate of intrest'))
si(p,t,r)

'''
A function can return a value
'''
def add(n1,n2):
    result = n1+n2
    #print('Result of addition ',result)
    return result
    
res = add(100,150)
print('result ',res)

'''
Write a function to find the sum of
digits of a given number by getting
user inputs

123 = 1+2+3 = 6
345 = 3+4+5 = 12
'''

def Sum(n):    
    sum = 0
    while (n != 0):      
        sum = sum +n % 10 
        n = n//10      
    return sum  

n = int(input("Enter a number"))

total = Sum(n)
print("Sum is " ,total)

'''
Step 1
n=123
sum = 0

123%10 = 3
sum = 0+3 = 3

n=123/10=12

step 2

sum = 3+ 12%10 
sum = 3+2 = 5
n=12/10
n=1

step3

sum = 3+2+1%10
sum = 3+2+1



1. Reverse a given number
526 - 625
2. Check the given number is palindrome or not
121 - 121
171 - 171
'''

n=int(input("Enter number: ")) #12
rev=0
while(n>0): #12 >0
    dig=n%10 #12%10-2 ---1%10 - 1
    rev=rev*10+dig #0x10+2 = 2X10+1
    n=n//10 #12//10 -1 1//10 - 0
print("Reverse of the number:",rev)

'''

2. Palindrome

'''
n=int(input("Enter number: ")) #12
original = n
rev=0
while(n>0): #12 >0
    dig=n%10 #12%10-2 ---1%10 - 1
    rev=rev*10+dig #0x10+2 = 2X10+1
    n=n//10 #12//10 -1 1//10 - 0
print("Reverse of the number:",rev)

if(original == rev):
    print(original, " It's palindrome")
else:
    print(original, " is not a palindrome")

'''
3. Fibonacci series

0 1
0+1 = 1
1+1 = 2
1+2 = 3
how many terms - 7
0 1 1 2 3 5 8
9
0 1 1 2 3 5 8 13 21
'''


terms = int(input("Enter a term"))
n1=0
n2=1
'''
print(n1)
print(n2)
'''
print(n1,end=' ')
print(n2,end=' ')
for i in range(terms-2):
    n3 = n1 + n2
    '''
    print(n3)
    '''
    print(n3,end=' ')
    n1 = n2
    n2 = n3

'''
Generate a * pattern by getting user
input

if no of stars is 5

*
* *
* * *
* * * *
* * * * *

Reverses
* * * * *
* * * *
* * *
* *
*
'''









    

    


