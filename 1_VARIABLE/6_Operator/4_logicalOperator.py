# Not Operator

a = 32
b = 66
print(not (b>a))

#example 
print(not False)
print(not True)

"""AND operator : In the "AND" operator the values comes true when the both values is true
    otherwise the answer will be the False.
"""

"""
    OR Operator : in the "OR" operator the values comes true when the one value or the both 
    values are true, in OR operator when the both value are false the the answer will also false.
"""
val1 = True
val2 = False
val3 = True
val4 = False

# Example about the AND operator
print("AND Operator answer is : ", val1 and val2)

# Example about the OR operator
print("OR Operator answer is : ", val2 or val3)

#Multiple experssion.
print("For 'And' Experession: ")
print("Answer for AND is: ", (a == b) and (a > b))
print("Answer for AND is: ", (a != b) and (a < b))

print("For 'Or' Experession: ")
print("The answer is : ", (a == b) or (a < b))