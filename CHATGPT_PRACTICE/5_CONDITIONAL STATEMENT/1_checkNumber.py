# Check whether a number is positive, negative, or zero.

# predefine
a = 10
if(a > 0):
    print("Positive Value : ")
elif(a == 0):
    print("Zero")
elif(a < 0):
    print("Neagative value :")

# User Define.
a = int(input("Enter Number : "))
if(a >= 0):
    print(a, "is Positive value ")
elif(a == 0):
    print(a, "this is zero")
elif(a < 0):
    print(a, "is Neagative value.")