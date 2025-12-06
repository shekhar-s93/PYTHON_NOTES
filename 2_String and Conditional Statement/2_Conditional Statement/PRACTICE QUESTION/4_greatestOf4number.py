a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
d = int(input("Enter Third Number: "))

if(a > b and a > c and a > d):
    print(a, "is the Greater.")

elif(b > c and b > d):
    print(b, "is the Greater.")

elif(c >= d):
    print(c, "is the Greater.")

else:
    print(d, "is the Greater.")