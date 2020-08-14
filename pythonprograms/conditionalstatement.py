# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 20:27:27 2020

@author: lenovo
"""

age = 19
if(age>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
    

age = int(input("Enter your age"))
if(age>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

'''
1. WAP to check whether a given number is
even or odd
'''
num = int(input("Enter the number "))
if(num%2==0):
    print("even")
else:
    print("odd")

'''
2. WAP to print the grade of a student based
on the marks..
marks>90 and marks<=100 - A+
marks>80 and marks<=90 - A
marks>70 and marks<=80 - B+
marks>60 and marks<=70 - B
marks>50 and marks<=60 - C+
marks>40 and marks<=50 - C
marks<=40 - F
'''
marks = int(input("Enter marks"))

if (marks>90 and marks<=100):
    print("A+")
elif (marks>80 and marks<=90):
    print("A")
elif (marks>70 and marks<=80):
    print("B+")
elif (marks>60 and marks<=70):
    print("B")
elif (marks>50 and marks<=60):
    print("C+")
elif (marks>40 and marks<=50):
    print("C")
else:
    print("F")
    
    
'''
3. eCommerce bill calculation

purchase<=10000  - 10 % discount
purchase>10000 and <=20000 - 20 %
purchase>20000 and <=30000 - 30 %
purchase>30000 - discount 40 %

Ask the user . How much he/she has purchased
Calculate the bill amount. 
Also show the dicount amount

10000*.1= 1000
billamount = 10000-1000
billamount = 9000
discount = 1000

'''

'''
4. Electricity bill calculation

units<=100 - Charges are 1 INR/Unit
units>100 and units <=200 - Charges are 2 INR/Unit
units>200 and units <=300 - Charges are 3 INR/Unit
units>3000 charges 4 INR/Unit

Calculate the bill amount by getting user input
of units consumed 

Sample calculation

unitsconsumed = 50 units

billamount = 50 X 1 = 50

unitsconsumed = 150 units

1st 100 units
billamount = 100 X 1 = 100
Rest 50 units

150-100 = 50 *2 = 100

Total bill = 100+100 = 200

'''
