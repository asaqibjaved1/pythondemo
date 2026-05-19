# Python Function 
def sum(a = 10,b = 5):
    return a + b
var = sum(23,43)
print(var)

var2 = sum()
print(var2)

def average(c,d):
    sum = c + d
    ave = sum/2
    return ave
var3 = average(34,54)
print(var3)

# WAF to print the length of a list.
animals = ["cat", "dog", "lion", "tiger"]
birds = ["parrot", "pigeon", "crow",]

def listlength(list):
    return print(len(list))

listlength(animals)
listlength(birds)

# WAF to print the elements of a list in a single line. ( list is the parameter)
animals = ["cat", "dog", "lion", "tiger"]

def listelements(list):
    for item in list:
        print(item, end=" ")

listelements(animals)