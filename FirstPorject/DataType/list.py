a= [2,3,4,5,"pisal"]
a[0]=7;
print("a[2]=",a[2])
print("a[0:3]",a[0:3])
print("a[3:]",a[2:])
print(type(a))
"""""tuple are immutable, tuple once created can not be modified"""""
t=(5,"pisal",1+3j)
print("t[2]=",t[2])

#t[1]
print("t[1]",t[1])
""""Python Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. 
Items in a set are not ordered."""""
print("Python set")
"""set do not support indexing"""
b = {2,3,4,5,6,7,8}
print(b)
#data type of b
print(type(b))
"""We can perform set operations like union, intersection on two sets. Set have unique values. They eliminate duplicates."""
d={1,1,2,3,2,4,3}
print(d)
