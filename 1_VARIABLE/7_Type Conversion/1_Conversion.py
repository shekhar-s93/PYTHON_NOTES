# two types of converstion in python 
# 1 = Conversion - Conversion autometically convert the data type according to their data type..

a, b = 2, 4.9
sum = a + b
print("Sum of different type of data is: " ,sum)

"""
    When perform the task between "integer" and "float" the answer always be a float value.
    and we also convert the "interger" and "float" value in "string" but we can't convert "string"
    in the "integer" and "float" value until the data as same. 

    For example: 
        You have a string variable 'a' and you assign the value "3266" in the string variable like this..
        a = "3266"

        you can convert this type of data in the "integer" and "float" data type.

        if you have this type of string data, a = "Shekhar", 
        then you can't convert into the "integer" and "float".

"""

# 2 = Casting - manually convert the data type 


c = 3.14
# type conversion of C variable
c = str(c)
print(type(c))

#Valid Conversion.
var_1 = "32"
var_2 = 66
print("Types of var_1: " ,type(var_1))
print("Types of var_2: " ,type(var_2))

#convert the type using 'Type Casting'
var_1 = int(var_1)
print("Converted type of Var_1 is : ", type(var_1))

#Now doing the sum of between var_1 and var_2

casting_Sum = var_1 + var_2
print("The Sum of casting type is : ", casting_Sum)

#Invalid Conversion.

d, e = 5, "9"
print(type(d))
print(type(e))

addtion = d + e
print(addtion)

"""
    Its gives error because here i don't convert string into the "integer" and "float", so
    its gives the error, if we converts its into the "integer or float" data type then it 
    not gives the error.
"""

#   [NOTES:] - Type casting when works, when you have such types of data which are fixed into the new data.


