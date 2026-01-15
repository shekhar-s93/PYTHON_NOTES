# find the largest of three number 

# predifine 
a = 10
b = 20
c = 30

if(a >= b and a >=c):
    print(a, "is Greater")
elif(b >= c):
    print(b, "is Greater")
else:
    print(c, "is Greater")

# User Define .
a = int(input("Enter first Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

if(a >= b and a >=c):
    print(a, "is Greater")
elif(b >= c):
    print(b, "is Greater")
else:
    print(c, "is Greater")