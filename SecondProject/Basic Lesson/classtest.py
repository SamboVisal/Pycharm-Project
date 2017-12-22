

class myClass():
    def method1(self):
        print("Hello world1")
class anotherClass(myClass):
    def method2(self,string):
        print(string)
    def method3(self):
        myClass.method1(self)
        print("anohter method 3")
def main():
    c = myClass()
   # c.method1()
    d = anotherClass()
    d.method2("Hello Pisal")
    d.method1()
    d.method2("new")
    d.method3()

if __name__ == '__main__':
    main()