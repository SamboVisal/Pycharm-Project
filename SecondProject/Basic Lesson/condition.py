x,y = 40,20
if x<y:
 st = "Y is greater than X"
elif x==y:
 st = "X and Y are equal"
else:
 st="X is greater than Y"
print(st)
#using loop
#python's range all parameters must be integers
print("using loop range")
for x in range(2,10,2):
 print(x)
print("using in loop")
music = ["Pisal","Michael","Smith"];
for i in (music):
 print(i);
for k in range(len(music)):
 print(music[k])
#define while loop
print("using while loop")
def main():
 x = 0;
 while(x<5):
  print(x)
  x+=1

if __name__ == '__main__':
    main();
print("using IN for collection")
day=["Mon","Tue","Wed","Thu","Fri","Sat"]
for d in day:
  print(d)

print("using break and continue")
for x in range(1,10):
 if(x==5): break
 print(x)
print("using continue")
#continue will skip the rest of the loop
for x in range(1,10):
 if(x%2==0): continue
 print(x)
#using enumerate to get the index
day=["Mon","Tue","Wed","Thu","Fri","Sat"]
print("using enumerate function")
for i,d in enumerate(day):
 print (i, d);
