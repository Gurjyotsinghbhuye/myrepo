# print('Hello World')

# datatypes 
# x = 4  # int
# x = 9.0 #
# x = "dd"
# x='A'
# x = True
# print(x,type(x))

# control statements
# age = 18
# if age < 17:
#     print('X')
# elif age > 18:
#     print('M or L')
# else:
#      print('invalid')
 

#  Loops 

# for i in range (5):
#     print(i)

# count = 0
# while count < 5 :
#     print (count)
#     count+=1

# define functions using def. def is a keyword in py
# def greet(name):
#     return f"Hello, {name}"
# what is f here ? for syntax? 
# print(greet('Karan'))

# Lists 
# Array in py are lists
# fruits = ['banana','Mango','Apple']
# print(fruits)

# # Access elements of fruits
# print(fruits[0])
# print(fruits[2])

# fruits.append('Cherry')

# Dictionaries
# A key value pair in python is called dictionaries
# stu = {['name' : 'Karan', 
#        'age'  : 18,
#        'Drinker':False,]
#        ['name' : 'Karan', 
#        'age'  : 18,
#        'Drinker':False,
#         ]}

# print (stu['age'])

# importing a module in py
# import  math as m
# print(m.sqrt(16))

# oops concepts

# class dog:
#     def __init__(self) 
#         self.
#     def bark(self):
#         return 'Woof'
    
# doge = dog 
# print(doge.bark)

# class calculator:

#     def plus(a,b):
#         return a+b
    
#     def plus(a,b,c):
#         return a+b+c
    
#     def mult(a,b):
#         return a*b
    
#     def Div(a,b):
#         return a/b
    

# cal = calculator
# # print(cal.plus(2,3))
# print(cal.mult(2,3))

# # fibonacci
 
# import math as m

# def rev(str):

#     a = len(str) -1
#     str2 = ''
#     while a >= 0:
#         str2 += str[a]
#         a-=1
#     print(str2)

# data = 'karan'
# if data== rev (data): 
#     print("Palindome")
# else: 
#     print("Not")

# lisr = 'ko'
# print(lisr[::-1])

# extract a part of string

# str = '      Pro+(gr&a_mm)ing ' 
# # splice
# print(str[5:9])
# # remove whitespace
# print(str.strip()) 

# index = str.find('Pro')
# str2= str.replace('Pro','worls]d')
# print(str2)

# Advanced functions
# str = '  Pro+(gr&a_mm)ing ' 
# splitted = str.split('+') after splitting it comes in a list
# print(splitted)

import random as r
a = 6
arr = []
while a > 0:
    arr.append(r.randint(0,100))
    a=a-1
print(arr) 

import numpy as np
arr1 = np.arange(10)
print("1D array:", arr1)

