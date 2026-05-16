# Python Dictionary
student = {
    "name" : "faizan",
    "marks" : 85,
    "grade" : "A",
    "class" : "10th"
}
print(student)
print(type(student))
student["name"] = "safeer" #change any key value in dict
print(student)

# list and tuple in dictionary
student1 = {
    "name" : "faizan",
    "marks" : 85,
    "grade" : "A",
    "class" : "10th",
    "subj" : ["bio", "che", "phy", "maths", "computer"],
    "period" : ("first", "third", "fourth")
}
print(student1) #print all values of dict
print(student1["subj"]) #print specific key value of dict

# Nesting in dictionaary
teacher = {
    "name" : "Saqib",
    "school" : "roots",
    "period" : {
        "first" : "AI",
        "Second" : "OS",
        "third" : "DDO"
    }
}
print(teacher) #calling whole dict
print(teacher["name"]) #calling name key
print(teacher["period"]["first"]) #calling the key of nested key of the dict teacher

# Methods in dictionary
print(teacher.keys()) #print all keys of dict
print(teacher.values()) #print all values of the key
print(len(teacher)) #print length of dict
print(teacher.get("name")) #print specific key through get method
teacher.update({"city" : "Haripur"}) #update the dictionary
print(teacher)
print(teacher.items()) #pritn all the key and values of dict as tuples

