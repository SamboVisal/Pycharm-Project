def insert(value,n):
    for i in range(0,n):

        key = value[i]
        pos = i

        while(pos>0 and key < value[pos-1]):
            print("Key " + str(key))
            print("Value "+ str(value[pos-1]))
            print("First Round")
            value[pos] = value[pos-1]
            pos = pos-1

        print(value)


value = [7,5,3,2]
n=len(value)
insert(value,n)
print(value)