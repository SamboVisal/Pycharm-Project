s='Hello Bitch'
# Strings are immutable in Python
print("The output is ",s)
print("s[0:4]",s[0:5])
print("s[3]",s[3])
#error
"""
s[3]='d'
print(s)
"""
saving = 100
factor = 1.1
result = saving*factor**7
print(int(result))
print("Your mmoney is $" + str(saving) + " and factor is " + str(factor)+"\n")
print("The total is " + str(result))