# Python Conditional Statements

marks = int(input("Enter Your marks"))
if(marks >= 90):
    grade = "A"
elif(marks >=80 and marks < 90):
    grade = "B"
elif(marks >=70 and marks < 80):
    grade = "C"
elif(marks >= 60 and marks < 70):
    grade = "D"
else:
    grade = "Fail"

print("Your grade is :", grade)
