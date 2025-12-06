light = "green"

if(light == "red"):
    print("Stop")

elif(light == "yellow"):
    print("Look out the your side")

elif(light == "green"):
    print("Go")

# You can write multiple if statement rather than elif.
# LIKE THIS

"""
        light = "green"

        if(light == "red"):
            print("Stop")

        if(light == "yellow"):
            print("Look out the your side")

        if(light == "green"):
            print("Go")

"""

#[NOTE] :- But you cann't write only elif statement in your code, because elif works when if condition is wrong.



# IF you write multiple "if" condition, and all "if" condition are correct then all statement of condition will print.

a = 10

if(a > 9):
    print("1 \t A is greater than 9")

if(a > 7):
    print("2 \t A is greater than 7")

if(a > 4):
    print("3 \t A is greater than 4")

if(a > 1):
    print("4 \t A is greater than 1")


# IF you use both condition "if & elif" or if and elif both condition are true then here only if statement are executed.

if(a > 9):
    print("5 \t A is greater than 9")

elif(a > 7):
    print("6 \t A is greater than 7")

elif(a > 4):
    print("7 \t A is greater than 4")


# There is one more important condition (else)
# The work of else condition is, if all the condition are wrong the this condition is executed.

# LIKE THIS

print("\nTraffic Light Example:")
trafficLight = "Orange"

if(trafficLight == "red"):
    print("8 You have to stop")

elif(trafficLight == "green"):
    print("9 You can go")

elif(trafficLight == "yellow"):
    print("10 You have to Lookout at your side")

else:
    print("11 Something is wrong")


# Student grade marks.
print("\nStudents Grade Example.")

marks = 59

if(marks <= 100 and marks >= 90):
    print("A - Grade")

elif(marks < 90 and marks >= 80):
    print("B - Grade")

elif(marks < 80 and marks >= 70):
    print("C - Grade")

elif(marks < 70 and marks >= 60):
    print("D - Grade")

else: 
    print("Your Are fail Buddy: ")



# NESTING CONDITION

# written condition into a condition is called nesting conditon.

# Were it use this conditon, Suppose you are above 18 years old you are able to drive vehicals and you are 80 years old then its not possible to drive any kind of vehicals.

print("\nNesting Condition Example: ")

age = 14

if(age >= 18):
    if(age >= 80):
        print("You can not drive.")
    else: 
        print("You can Drive.")

else:
    print("You are under age, so you can not drive")
