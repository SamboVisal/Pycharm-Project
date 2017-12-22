
num=int(input("Enter number to check "))

if num > 1:
    for i in range(2,num):
        if(num%i)==0:
            print("This is not prime")
            break;
    else:
            print("This is prime")
else:
    print("Positive numers pls")
    
    