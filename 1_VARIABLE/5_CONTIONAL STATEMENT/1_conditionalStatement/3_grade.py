marks = int(input("Enter your marks: "))

if(marks >= 90):
    print("A - Grade.")

elif(marks < 90 and marks >= 80):
    print("B - Grade.")

elif(marks < 80 and marks >= 70):
    print("C - Grade.")

else:
    print("D - Grade.")