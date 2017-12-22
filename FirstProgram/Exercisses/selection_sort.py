value = [7, 5, 4, 2];
n = len(value)
for i in range(0, n):
    m = i
    for j in range(i+1,n):
        if (value[j] < value[m]):
            m = j
    temp = value[m]
    value[m] = value[i]
    value[i] = temp

print(value)


