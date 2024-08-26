#USERDEFINED TYPE
#1. They can't retun->non return
#2. They can return something
#3.They have parameters
#4.They dont have parameters
import sys

#1. They can't retun->non return

#no return type no parameter
def greet():
    print("hello")


result=greet()
print(result)



#no return type with parameter
def greet(name):
    print("hello",name)


result=greet("rohit")
print(result)




#no return type with default parameter/args
def greet(name="Rohit"):
    print("hello",name)


result=greet()
print(result)
result=greet("Amit")
print(result)
result=greet(name="Amit")
print(result)


#no return type with multiple parameter/args
def greet(name1,name2,name3):
    print("hello",name1,name2,name3)


result=greet("Ram","mukul","deepshikha")
print(result)

#argument +return type
def sum_of_two_number(num1,num2):
    return num1+num2

def sum_of_two_number_wih_default(num1=20,num2=30):
    return num1+num2


result=sum_of_two_number(12,34)
print(result)

result=sum_of_two_number_wih_default()
print(result)

