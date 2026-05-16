#Sets in Python
# Set is unordered
# Set remove duplicate values
# Set only count unique values
set1 = {1,3,3,4,5,5,5}
print(set1)
print(len(set1))

set2 = set() #empty set syntax
print(set2)
print(type(set2))

#Sets methods
set2.add(2) #add method
set2.add(5)
print(set2.pop()) #pop method
print(set2)
set2.clear() #clear method
print(set2)

a = {1,2,3}
b = {3,4,5}
print(a)
print(b)
print(a.union(b)) #union of two sets
print(a.intersection(b)) #intersection of two sets