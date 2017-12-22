from datetime import date;
from datetime import time;
from datetime import datetime;
#using function

def func1():
    print("I am a function")
#func1()
#func1 is calling and it needs a return value otherwise it will print none below
print(func1())
print(func1)
#function takes 2 arguments
print("Function takes 2 arguments")
def func2(arg,arg2):
    print(arg, " ",arg2)
    return arg*arg2;
func2(10,20)
print(func2(20,50))
print("Function with return value")
def cube(x):
    return x*x*x
print(cube(3))
#function with default value
print("function with default value")
def power(num,x=1):
    result = 1;
    for i in range(x):
        result = result * num;
    return result;
print(power(2))
print(power(3,3))
#reverse argument
print(power(x=3,num=2))
#Function with variable of argument
#* means will take all of varibles that will be called
def multi_add(*args):
    result = 0;
    for i in range(args):
        result = result + args;
    #put result this line or else it will not return cuz in different line
    return result;
#print (multi_add(4,5,6,7,8));

def fun(self):
    print("Hello world ",self)

n = "pisal"
fun(n)