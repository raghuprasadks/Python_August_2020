# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:26:01 2020

@author: lenovo
"""

'''
Multi line Comments

Operators

1. Arithmetic Operators - +,-,*,/,//,%,**


'''
#single line comment

n1=100
n2=250

n3=n1+n2
print('Result of Addition ',n3)

n3=n1-n2
print('Result of Subtraction ',n3)

n3=n1*n2
print('Result of Multiplication ',n3)

n3=n2/n1
print('Result of Division - / ',n3)

'''
250//100
'''
n3=n2//n1
print('Result of Division - // ',n3)
'''
% remainder
'''
n4=9
n5=2
n6=n4%n5
print("Result of % ",n6)
'''
Exponent 2**3 = 2*2*2 = 8
'''
n7=2
print("Result of ** ",n7**3)

'''
2. Relational Operators - >,<,<=,>=,==,!=
'''
n1=100
n2=150
n3=200
n4=150
print("n1 > n2",n1>n2)
result = n2>n1
print("n2 > n1 ",result)

result = n2<n1
print("n2 < n1 ",result)

result = n2<=n4
print("n2 <= n4 ",result)

result = n2>=n4
print("n2 >= n4 ",result)

result = (n2==n4)
print("n2 == n4 ",result)

result = (n1!=n4)
print("n1 != n4 ",result)

'''
3. Logical Operators - and, or, not
'''
n1=100
n2=50
n3=200

result = (n1>n2) and (n3>n2)
print('result of and ',result)

result = (n1<n2) and (n3>n2)
print('result of and ... ',result)

result = (n1<n2) or (n3>n2)
print('result of or ... ',result)

result = not (n1<n2)
print('result of not ... ',result)




