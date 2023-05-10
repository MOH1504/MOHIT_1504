"""
Dictionary : which is contain key and value in a pair.

syntax :

dictionary = {
    "key" : value,
    "key" : value,
}

"""
"""
student = {
    "name" : "jay",
    "subject" : "python",

}
print(student)
print(student["name"])
print(student["subject"])

student ["subject"] = "java"

print(student)
"""

"""

Quiz = {
    1 : {
        "que" : "which is most popular programing language",
        "ans" : "python"
    },
    2 : {
        "que" : "who is develope c language",
        "ans" : "Danis"
    }
}

print(Quiz[1]["que"])
ans = input("Enter your ans : ")
if ans == Quiz[1]["ans"]:
    print("right answer")
else:
    print("wrong answer")
    
"""
"""

Quiz = {
    1 : {
        "que" : "which is most popular programing language",
        "ans" : "python"
    },
    2 : {
        "que" : "who is develope c language",
        "ans" : "Danis"
    }
}

for i in range(1,len(Quiz)+1):
    print()
    print(Quiz[i]["que"])
    ans = input("Enter your ans : ")
    if ans == Quiz[i]["ans"]:
        print("Right ans : ")
    else:
        print("Wrong ans : ")

"""
Right_ans_count = 0
Wrong_ans_count = 0

Quiz = {
    1 : {
        "que" : "which is most popular programing language",
        "ans" : "python"
    },
    2 : {
        "que" : "who is develope c language",
        "ans" : "danis"
    },
    3 : {
        "que" : "Who is world best cricketer",
        "ans" : "virat kohli"
    },
    4 : {
        "que" : "who is prime minister of india",
        "ans" : "narendra modi"
    },
    5 : {
        "que" : "how many world population",
        "ans" : "8 billion"
    } 
}

for i in range(1,len(Quiz)+1):
    print()
    print(Quiz[i]["que"])
    ans = input("Enter your ans : ")
    if ans == Quiz[i]["ans"]:
        Right_ans_count += 1
    else:
        Wrong_ans_count += 1

print("Right ans : ",Right_ans_count)
print("Wrong ans : ",Wrong_ans_count)        
