light = "green"

if(light == "Yellow"):
    print("You have to ready for go: ")
elif(light == "red"):
    print("You have to stop")
elif(light == "green"):
    print("Now you can go ")
else:
    print("Someting went wronge ")

num = 15
if(num % 2 == 0):
    print("Even number : ")
else:
    print("Odd Number")

a = 100
b = 44
c = 100

if(a > b and a > c):
    print("A is greater than B and C")
elif(b > c):
    print("B is grater than A and C")
else:
    print("C is greater.")

num7 = 72

if(num7 % 7 == 0):
    print(num7, "is multiple of Number 7")
else:
    print(num7, "is not multiple of Numebr 7")


# Now Print the greatest of 4 number 
num1 = 99
num2 = 100
num3 = 300
num4 = 40

if(num1 > num2 and num1 > num3 and num1 > num4):
    print(num1, "is greater from all.")
elif(num2 > num3 and num2 > num4):
    print(num2, "is Greater from all")
elif(num3 > num4):
    print(num3, "is greater from all")
else: 
    print(num4, "is greater from all")

# Assigning the grade.

marks = 79
if(marks <= 100 and marks >= 90 ):
    print("A Grade")
elif(marks < 90 and marks >= 80):
    print("B Grade")
elif(marks < 80 and marks >= 70):
    print("C Grade")
elif(marks < 70 and marks >= 60):
    print("D Grade")
else:
    print("Fail")