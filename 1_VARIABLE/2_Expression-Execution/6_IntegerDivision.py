#Integer Division with float and int will give int displayed as float
# // between two operand is called integer division like (a//b)

a, b = 1.5, 3
c = a//b
print(c, a/b)

"""
floor gives closest integer, which is lesser than equal to the float value Result of (a//b) is same as floor(a/b)
"""

a, b = 12, 5
c = a//b
print(c)

a, b = -12, 5
c = a//b
print(c)

# here answer is -3 insted of -2 because -3 is smallest than -2

a,b = 12, -5
c = a//b
print(c)

