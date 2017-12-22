num=int(input("Enter number "))
result=0;
te = num
while num>0:
    re = num%10
    result += re*re*re
    num//=10
if (result==te):
    print("This is armstrong number",result)
else:
    print("This is not armstrong",result)