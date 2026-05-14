# WAP to check if a number entered by the user is odd or even.
num1 = int(input("Enter a number to check it is even or odd"))
reminder = num1 % 2
if (reminder == 0):
    result = "Even"
else:
    result = "odd"
print("You entered number is : ", result) 

# WAP to find the greatest of 3 numbers entered by the user.
print("Enter three numbers. I will tell you which will be the greatest")
num2 = int(input("Enter the first number"))
num3 = int(input("Enter the second number"))
num4 = int(input("Enter the Third number"))
if (num2 >=num3 and num2 >= num4):
    result = num2
elif (num3 >= num4):
    result = num3
else: result = num4
print("The greatest among the three is :", result)


# WAP to check if a number is a multiple of 7 or not.
print("Enter any number and I will tell you it is multiple of 7 or not")
a = int(input("Enter the first number"))
if(a % 7 == 0):
    print("It is multiple of 7: ")
else:
    print("It is not muultiple of 7 :")

    print("End of program")