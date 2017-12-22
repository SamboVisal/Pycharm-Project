
from datetime import date;
from datetime import time;
from datetime import datetime
print("using class");
class myClass():

    def method(self):
        print("This is the first method")
    def method1(self,string):
        print("This is " + string)
class anotherClass(myClass):
    def method1(self):
        print("This is another class method1")
    def method(self):
        myClass.method(self);
        print("another class method ")
def main():
    
    c = myClass()
    c.method();
    c.method1("Method the second")
    print("This is Using another Class Statement")
    c2= anotherClass()
    c2.method();
    c2.method1();
    today = date.today();
    print("Date component ",today.day,today.month,today.year)
if __name__ == '__main__':
    main()

