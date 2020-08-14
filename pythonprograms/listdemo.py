# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 20:21:29 2020

@author: lenovo

list
"""
'''
list
'''
fruits=['banana','apple','guava']
print(fruits)
print(type(fruits))
#<class 'list'>
print(len(fruits))

'''
append
list allows duplicate values
'''
fruits.append('mango')
print('after append ',fruits)

fruits.append('orange')
print('after append ',fruits)

'''
update

'''
print(fruits[0])

fruits[3]='pine-apple'
print('after updation ',fruits)

'''
print all the elements in the list
'''
for i in fruits:
    print(i)
    
'''
delete
'''
del fruits[0]
print(fruits)
#delete the last elments in the list
fruits.pop()

#deleles a specific element in the list
fruits.remove('guava')

'''
Insert element at a specific position
'''
fruits.insert(1,'mango')

'''
create a list of invitees to a function
'''

friends=[]

nooffriends = int(input("how many friends to invite"))

for i in range(nooffriends):
    name = input('name of the person to invite')
    friends.append(name)
print('list of invitees ',friends)


'''
Your mother gives a list of groceries to purchase
from a shop..
prepare a list of 10 groceries which your mother told
you to buy

1. do not buy item 3 in the list
2. In place of item 3 buy milk
3. Buy banana and coconut additionally

'''    

noofstars = int(input('Enter number of stars'))
for i in range(0,noofstars):
    for j in range(0,i+1):
        print('*',end=" ")
    print()
    
groc = []
n = int(input('Enter the number of groceries to buy : '))
for i in range(n):
    name = input('Enter the grocery list :')
    groc.append(name)
print('The list of groceries are ', groc)
groc[2] = 'Milk'
print('The list of groceries after replacing ', groc)
groc.append('Banana')
print('The list of groceries after additional requirement1 ', groc)
groc.append('Coconut')
print('The list of groceries after additional requirement1 ', groc)
    

'''
range(0,4)
0
1
2
3
range(5,10)
5
6
7
8
9
'''

'''
slicing
'''
numlist=[1,3,6,8,10,12]
print(numlist)
newlist = numlist[1:3]
print('new list ',newlist)
list2 = numlist[3:7]
print('list2 ',list2)
print(numlist[-1])
print(numlist[-3])

'''
cancatenation
'''
list1=[1,2,3]
list2=[5,6,7]
list3 = list1+list2
print('list 3',list3)

'''
max,min,sum,average
'''
data=[2,3,5,18,8,10,12,1]
print('maximum ',max(data))
print('minimum ',min(data))
print('sum ',sum(data))
print('Average ',sum(data)/len(data))


'''
Corona Dashboard
'''
coronadashboard=[]
header=['Name','Total','Positive','Recovered','Dead']
coronadashboard.append(header)
print('coronadash board',coronadashboard)
karnataka=['Karnataka',100000,40000,50000,10000]
coronadashboard.append(karnataka)
tamilnadu=['Tamil Nadu',1200000,50000,55000,15000]
coronadashboard.append(tamilnadu)
print('Final dashboard ',coronadashboard)


'''
display
'''
for i in coronadashboard:
    print(i)

'''
ipl
'''
ipldashboard=[]
players=[['name','team','match','runs','wickets']]
ipldashboard.append(players)
print('ipl dashboard',ipldashboard)
a=['virat','RCB',12,600,0]
ipldashboard.append(a)
b=['ABD','RCB',8,480,0]
ipldashboard.append(b)
c=['Jadeja','CSK',12,300,5]
ipldashboard.append(c)
print('final dashboard ',ipldashboard)
for i in players:
    print (i)
    
'''
ReportCard
'''
reportcard=[]
header=['name','regno','sub1','sub2','sub3','total']
reportcard.append(header)
noofstud = int(input('Enter number of students'))

for i in range(noofstud):
    stud=[]
    name = input('Enter name')
    regno=int(input('Enter regno'))
    sub1=int(input('Enter sub1'))
    sub2=int(input('Enter sub2'))
    sub3=int(input('Enter sub3'))
    total=int(input('Enter total'))
    stud.append(name)
    stud.append(regno)
    stud.append(sub1)
    stud.append(sub2)
    stud.append(sub3)
    stud.append(total)
    reportcard.append(stud)
print('report card',reportcard)    
    
    
    
    

    
    
    
    
    
    
					

























