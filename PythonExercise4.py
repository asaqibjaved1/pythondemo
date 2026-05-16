# Store following word meanings in a python dictionary :
# table : “a piece of furniture”,“list of facts & figures”
# cat : “a small animal”
wordmean = {
    "table" : ["a piece of furniture" , "list of facts & figures"],
    "cat" : "a small animal"
}
print(wordmean)

# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”
cour = {
    "python","java","C++","python","javascript","java","python","java","C++","C"
}
print(cour)
print(len(cour))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#  Start with an empty dictionary & add one by one. Use subject name as key
#  & marks as value.
subj = {
    "che" : "",
    "phy" : "",
    "bio" : ""
}
sub1 = input("Enter your chemistry marks :")
subj["che"] = sub1

sub2 = input("Enter your Physics marks :")
subj.update({"phy" : sub2}) #another method

sub3 = input("Enter your Biology marks :")
subj["bio"] = sub3
print(subj)
print(type(subj))

# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
set1 = {9, "9.0"}
print(set1)
print(type(set1))

set2 = {
    ("int",9),
    ("float", 9.0)
}
print(set2)
print(type(set2))




