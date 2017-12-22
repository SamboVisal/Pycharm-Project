"""The sep separator is used between the values. It defaults into a space character.
After all values are printed, end is printed. It defaults into a new line.
The file is the object where the values are printed and its default value is sys.stdout (screen). Here are an example to illustrate this."""

print(1,2,3,4,sep='*',end='&' +" \n" )
"""We can even use keyword arguments to format the string."""
print("Hello {name} ,{greeting}".format(name="Pisal",greeting="How do u do?"))
a=21.34512
print('The value a is %.3f' %a)
k = input("Enter name ")
print("The name is ",k)
