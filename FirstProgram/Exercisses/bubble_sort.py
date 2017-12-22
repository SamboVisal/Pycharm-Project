def bubble(value,n):
    for i in range(0,n):
        for j in range(i+1,n):
            temp = value[i]
            value[i] = value[j]
            value[j] = temp


value = [7,5,4,2]
n = len(value)
bubble(value,n)
print(value)

