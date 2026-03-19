

# a="Ann"
# print(a)
# b=20
# print(b)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# avg=(a+b+c)/3
# print("The average is",avg)

#find the area
# L = int(input("Enter the length:"))
# W = int(input("Enter the width:"))
# Area = L*W
# print("Area is:",Area)

#Swapping
# a=4
# b=2
# a,b = b,a
# print("after swapping:")
# print(a)
# print(b)

#find the temp
# a=float(input("Enter the temperature in celsius:"))
# f=(a*9/5)+32
# print("The temperature is",f)

#find perimeter
# a=int(input("Enter the first number:"))
# b=int(input("Enter the second number:"))
# p=2*(a+b)
# print("the perimeter is",p)

# minutes = int(input("Enter minutes: "))
# seconds = minutes * 60
# print("Seconds:", seconds)

##logical operators
##AND
# a = 10
# b = 5
# print(a > 5 and b > 2)

##OR
# a=10
# b=5
# print(a > 5 or b > 10)

## comparison operators
# a=10
# b=5
# print(a==b)
# print(a!=b)
# print(a>b)
# print(a<b)
# print(a<=b)
# print(a>=b)

#assignment operators
# a=10
# a += 5
# print(a)
# b=20
# b -=5
# print(b)
# c=2
# c *=2
# print(c)
# d=5
# d /=2
# print(d)

#conditional statements

# age=int(input("enter your age:"))
# if age >= 18:
#    print("the age is eligible")
   
# else:
#    print("not eligible age<18")

# score=int(input("enter your score:"))
# if score>45:
#     print("A+")
# elif score>40:
#     print("A")
# elif score>35:
#     print("B+")
# elif score>30:
#     print("B")
# elif score>25:
#     print("C+")
# elif score>20:
#     print("C")
# else:
#     score<20
#     print("FAILED")


##for loop
# for i in range(1,6):
#     print(i)

##while loop
# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1

## array 
# arr = [10, 20, 30, 40, 50]
# # print(arr[0])
# # print(arr[1])
# print(arr[2])
# # print(arr[3])
# # print(arr[4])

##list
# list = [10, 20, 30, 40]
# list.append(50)
# list.remove(10)
# print(list)

##tuple
# data = (1, 2, 3, 4)
# print(data)

## find the sum of list elements
#list[10,20,30,40]
# numbers = [10, 20, 30, 40]
# total = 0
# for i in numbers:
#     total = total + i
# print("Sum:", total)

##count
# numbers = [10, 20, 30, 40]
# count = 0
# for i in numbers:
#     count = count + 1

# print("Number of elements:", count)

## search a number
# search=int(input("enter a number:"))
# numbers = [10, 20, 30, 40]
# if search in numbers:
#         print("Number found")
# else:
#         print("number not found")

# student=("ANJIMA",20)
# print("my name is",student[0])
# print("my age is",student[1])

##reverse
# numbers = [10, 20, 30, 40]
# numbers.reverse()
# print(numbers)

##CLASS
## A class is a blueprint or template used to create objects.
##OBJECT
##An object is an instance of a class.
# class Student:
#     name="Ann"
# s1 = Student()
# print(s1.name)

# class Message:
#     name = "Hello Ann"
# m1 = Message()
# print(m1.name)

##Constructor
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# s1 = Student("Ann", 20)
# print("Name:", s1.name)
# print("Age:", s1.age)

##inheritance
# class Animal:
#     def sound (self):
#         print("Animal Sound")
# class dog(Animal):
#     def bark(self):
#         print("dog barked")
# d=dog()
# d.sound()
# d.bark()

##polymorphims
# class Bird:
#     def sound(self):
#         print("chip chip")
# class Dog:
#     def sound(self):
#         print("bow bow")
# b = Bird()
# d = Dog()
# b.sound()
# d.sound()

##encpsulation
# Encapsulation
# class Bank:
#     def __init__(self):
#         self._balance = 1000
#     def show_balance(self):
#         print(self._balance)
# b = Bank()
# b.show_balance()


# Abstraction
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Square(Shape):
#     def area(self):
#         print("Area of square")
# s = Square()
# s.area()