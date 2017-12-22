#variable expression

#declare variable and initialize it
f = 0
print(f)
#re-declare varible
f = "abc"
print(f)
#cannot combine concatenate string and interger like "hi" + 123, you have to convert in below
print("I am string " + str(123))
#global and local function
print("Global vs Local variable")
i = 1997
print(i)
def someFunction():
    #this i is belong in this function only unless don't comment global
    #global i
    i="Hello World"
    print(i)

someFunction()
print(i)
#delete variable
print("Delete variable")
a = 0;
print(a)
del a
print(a)