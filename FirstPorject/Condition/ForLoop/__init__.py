"""The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
Syntax of for Loop
for val in sequence:
	Body of for"""

number =[2,3,4,5,6,7,9];
sum=0;
for i in number:
    sum=sum+i

print("The sum is %d ",sum)
print("Using range()")
print(list(range(10)))
print(range(11))
print("using rang(2,10)")
print(list(range(2,10)))
print("rang(2,10,2) each time increase by 2")
print(list(range(2,10,2)))
music=['pisal','michael','smith'];
for i in range(len(music)):
    print(music[i]);
print("ForLoop with else")
n = {2,1,1,6,9};
for i in n:
    print(i)
else:
    print("NTH left")