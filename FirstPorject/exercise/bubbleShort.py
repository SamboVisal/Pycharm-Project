value = [2,4,5,6,1,0]
for i in range(0,len(value)):
	for j in range(len(value)):
		if(value[i]<value[j]):
			temp = value[i]
			value[i] = value[j]
			value[j] = temp

print(value)