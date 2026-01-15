# Use parentheses to change the result of an expression.

# predefine

a = 5
b = 10
c = 3
d = 2

result = a + b + c + d
print("1.   Addition : ",result)

result = a * b + c*(c - d)
print("2.   Mixing : ", result)


# By user 
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))

result = a * b - d + (c * d)

print("final result : ", result)