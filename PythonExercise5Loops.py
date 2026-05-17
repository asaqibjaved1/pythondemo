# Python Loops Exercise
# Print numbers from 1 to 100.
# i = 1 
# while i <= 100:
#     print("Number : ", i)
#     i += 1
# print ("Program Ended")

# Print numbers from 100 to 1.
# j = 100
# while j >= 1:
#     print("Number : ", j)
#     j -= 1
# print ("Program Ended")  

# Print the multiplication table of a number n.
# l = 1
# while l <= 10 :
#         print( 4 * l)
#         l += 1

# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# list1 = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i = 0
# while (i < len(list1)):
#     print(list1[i])
#     i += 1

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)
x = 49
i = 0
while (i < len(tup)):
    if (tup[i] == 49):
        print("Found the number at position : ", i + 1)
    i += 1