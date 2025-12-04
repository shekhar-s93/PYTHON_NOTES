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

c = 3.14
# type conversion of C variable
c = str(c)
print(type(c))
