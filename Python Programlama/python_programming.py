# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 17:13:59 2023

@author: Lenovo
"""

# Numbers ve Strings
type(9)
type(9.2)

#String
type(123)
type('123')

'a'+'b'
'a'*3

#String Methods
str1='hello'
len(str1)
#Upper & Lower
str2=str1.upper()
str2

str1=str2.lower()
str1

#Checking
str1.islower()
str2.isupper()

#Replace
str1=str1.replace("e", "b")
str1


#Strip default = deleting space
str3='sa das '
str3.strip()

str3='*Asa*as*'
str3.strip('*')

#All methods
dir(str)
str1.capitalize()
str3.title()

str1[1]

str1[0:3]

#Variables
a=9999

b='Ali_uzaya_gitti'

first_number=input()
second_number=input()

int(first_number+second_number)

##########
print('hello','world',sep='-')

#%% Data Structures
#Lists Inclusive Ordered Changeable
nots=[90,80,70,50]
type(nots)

list1=['a',19.3,90]
list2=['a',19.3,90,nots]

len(list2)

type(list2[3])


#Merge Lists
merged_list=[list1,list2]

del merged_list

#Element operations
list1=[10,20,30,40,50]

list1[0]#first index

list1[0:2]#from the beginning of the list to the second index

list1[:2]#from the beginning of the list to the second index

list1[2:]#from the second index to the end

list2[3][2]#access the element of the inner list in a nested list


#Adding, Changing and Deleting Elements

list1=['ali','veli','berkcan','ayse']

list1[1]='velinin babasi'


list1[0:3]='alinin_babasi','velinin_babasi','berkcanin_babasi'

#append
list1.append('kemal')
#remove
list1.remove('kemal')

#insert
list1.insert(0, 'harun')

#pop
list1.pop(0)

#count
list2=['ali','ali','ali','veli','berkcan','ayse']
list2.count('ali')

#copy
copied_list=list2.copy()
#extend
list1.extend(list2)
#index
list1.index('ali')
#reverse
list1.reverse()
#sort
number_list=[312,1,32,89,97,67]
number_list.sort()

#%%Tuple Inclusive Ordered Unchangeable
t1=('ali','veli',1,2,3.4,[1,2,3,4])

t2='ali','veli',1,2,3.4,[1,2,3,4]

#Element operations
t1[1]

t1[0:3]
#Tuples elements can't change

#%%Dictionary Inclusive  Unordered Changeable

dict1={'REG':'Regression Model',
       'LOG':'Logistic Regression',
       'CART':'Classification and Regression'}

dict1

len(dict1)

dict2={'REG':['Regression Model',10],
       'LOG':['Logistic Regression',20],
       'CART':['Classification and Regression',30]}

#Element operations
dict1['REG']
dict1['LOG']

dict2['REG']


dict3={'REG':{'REG':'Regression Model',
              'LOG':'Logistic Regression',
              'CART':'Classification and Regression'},
       'LOG':{'REG':'Regression Model',
              'LOG':'Logistic Regression',
              'CART':'Classification and Regression'},
       'CART':{'REG':'Regression Model',
              'LOG':'Logistic Regression',
              'CART':'Classification and Regression'}}

dict3['REG']['REG']


#Adding, Changing and Deleting Elements

dict1['GBM']='Gradient Boosting Mac'
dict1

dict1['REG']='NEW Regression Model'
dict1


dict1[1]='Artificial Neural Networks'
dict1

# l=[1,2,3]
#Keys cannot be list
# dict1[l]='New'


l=(1,2,3)
#Keys can be tuple
dict1[l]='New'

dict1

#%% Sets Inclusive  Unordered Changeable Unique

l=[1,'a','ali',123]
set1=set(l)

set1

list2=['ali','lutfen','ata','bakma','uzaya','git','git','ali','git']

set2=set(list2)

set2

len(set2)

#Adding, Changing and Deleting Elements

l=['gelecegi','yazanlar']
set3=set(l)
#add
set3.add('ile')
set3

set3.add('gelecege_git')

set3.add('ali')
#add
set3.remove('ali')
#discard
set3.discard('ali')

#difference& symmetric_difference

set4=set([1,3,5])

set5=set([1,2,3])
# difference
set4.difference(set5)# just checking the difference #set4-set5

set5.difference(set4)
# symmetric_difference
set4.symmetric_difference(set5) #control both at the same time


#Intersection & union
set4.intersection(set5)#set4 & set5

set4.union(set5)

set4.intersection_update(set5)

set4

#Query
set6=set([7,8,9])

set7=set([5,6,7,8,9,10])

set6.isdisjoint(set7)#Is the intersection empty?

set6.issubset(set7)#Is it a subset?

set7.issuperset(set6)#Is it a superset?

#%%Functions

def squaring(x):
    print(x**2)

squaring(10)

def squaring(x):
    print("Girdiginiz sayi:"+ str(x) + 
          ", Karesi: " + str(x**2))

squaring(3)


def multiplication(x,y):
    print(x*y)

multiplication(2, 3)


def multiplication(x,y=1):
    print(x*y)

multiplication(2)
multiplication(2, 3)

def pole_calculation(heat,humidity,charge):
   print((heat+humidity)/charge) 
    
pole_calculation(25, 40, 70)

def pole_calculation_with_return(heat,humidity,charge):
   return (heat+humidity)/charge

value=pole_calculation_with_return(25, 40, 70)
value

#%% Local and Global Variable

x=10
y=20

def multiplication(x,y):
    return x*y

multiplication(2,3)

#Changing Global Domain from Local Domain
z=[]
def add_element(y):
    z.append(y)
    print(z)

add_element(10)
add_element(21)

#%%Decision control structures

limit=50000

income1=60000
income2=50000
income3=35000

if income3 > limit:
    print("Gelir sinirdan buyuk")
elif income3 <limit:
    print("Gelir sinirdan kucuk")
else:
    print("Gelir sinira esit")



#%% Example
limit=50000
shop_name=input("Magaza adi nedir? : ")
income=int(input("Gelirinizi girin: "))


if income > limit:
    print("Tebrikler! " + shop_name +" promosyon kazandiniz")
elif income <limit:
    print("Uyari! Cok dusuk gelir: "+str(income))
else:
    print("Takibe devam")

#%% Loops 

#For
list1=['ali','veli','isik','berk']

for i in list1 :
    print(i)

print('----------------')
list2=[1000,2000,3000,4000,5000]

for i in list2:
    print(i)

print('----------------')

def raise_salary_20(x):
    print( x*20/100+ x)

def raise_salary_10(x):
    print( x*10/100+ x)


for i in list2:
    raise_salary_20(i)
    
print('----------------')

for i in list2:
    if i>=3000:
        raise_salary_10(i)
    else:
        raise_salary_20(i)


#%%break& continue

list2=[8000,5000,2000,1000,3000,7000,1000]

list2.sort()

for i in list2:
    if i==3000:
        print("kesildi")
        break
    print(i)


print('----------------')

for i in list2:
    if i==3000:
        continue
    print(i)


#%% While

number=1
while number< 10:
    number +=1
    print(number)

#%% OOP

#Class

# class DataScientist():
#     print("Bu bir siniftir")


#Class attributes

class DataScientist():
    section=""
    sql="Evet"
    years_of_experience=0
    languages_knows=[]

#Accessing  Class attributes
DataScientist.section
DataScientist.sql

#Changing Class attributes
DataScientist.sql="Hayir"
DataScientist.sql

#Instantiation 

ali= DataScientist()

ali.sql
ali.years_of_experience
ali.section
ali.languages_knows.append("Python")
ali.languages_knows

veli=DataScientist()
veli.sql

veli.languages_knows
#%% 

class DataScientist():
    languages_knows=["R","Python"]
    section=""
    sql=""
    years_of_experience=0
    def __init__(self):
        self.languages_knows=[]
        self.section=""
        self.sql=""
        

ali=DataScientist()
ali.languages_knows

veli=DataScientist()
veli.languages_knows

ali.languages_knows.append("Python")

veli.languages_knows.append("R")
veli.languages_knows

#%% sample methods

class DataScientist():
    employee=[]
    def __init__(self):
        self.languages_knows=[]
        self.section=""
    def add_language(self,new_language):
        self.languages_knows.append(new_language)
        
        
dir(DataScientist())        
     
ali=DataScientist()
ali.add_language("Python")

veli=DataScientist()
veli.add_language("R")


#%% Inheritance

class Employee():
    def __init__(self):
        self.FirstName=""
        self.LastName=""
        self.Address=""

class DataScience(Employee):
    def __init__(self):
        self.Programming=""
        
class Marketing(Employee):
    def __init__(self):
        self.StoryTelling=""
        
ds1=DataScience()
ds1

mar1=Marketing()
mar1



class Employee_New():
    def __init__(self,FirstName,LastName,Address):
        self.FirstName=FirstName
        self.LastName=LastName
        self.Address=Address


ali=Employee_New('a', 'b','c')


#%%Functional Programming

#Pure Functions

#dependent
A=5

def impure_sum(b):
    return b+A
#Independent
def pure_sum(a,b):
    return a+b

impure_sum(6)
pure_sum(3, 4)


#Anonymous Functions

def old_sum(a,b):
    return a+b
old_sum(4, 5)

new_sum=lambda a,b:a+b
new_sum(4,5)

unsorted_list=[('b',3),('a',8),('d',12),('c',1)]

sorted(unsorted_list,key=lambda x:x[1])

#Vectorel Operations

#oop
a=[1,2,3,4]
b=[2,3,4,5]

ab=[]

for i in range(0,len(a)):
    ab.append(a[i]*b[i])

ab

#FP
import numpy as np
a=np.array([1,2,3,4])
b=np.array([2,3,4,5])

a*b

#Map&filter&reduce

list1=[1,2,3,4,5]

#map
list(map(lambda x:x+10,list1))

#filter
list1=[1,2,3,4,5,6,7,8,9,10]

even_number=list(filter(lambda x:x%2==0, list1))
even_number

#reduce
from functools import reduce

list1=[1,2,3,4]
reduce(lambda a,b: a+b ,list1)

#%%  Create a module

import calculate as cc
cc.raise_salary_20(100)

cc.salary

#%% try exceptions

#ZeroDivisionError
a=10
b=0


try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sifir olmaz")


a=10
b='2'


try:
    print(a+b)
except TypeError:
    print("Tip uyusmazligi")










