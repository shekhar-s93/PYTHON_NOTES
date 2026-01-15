# List in Python

# A built-in data type that stores set of values
# It can store elements of different types (Integer, float, string, etc.)

marks = [87, 65, 33, 95, 76] #marks[0], marks[1].....

student = ["Karan", 85, "Delhi"] #student[0], student[1].....

student[0] = "Shekhar"  # allowed in python

len(student) # returns length


# NOTE : In python Lists are mutable and String are immutable.

# mutable means change able the value

#   For Example : 
Student_name = ["Shekhar", 21, "Mumbai"]
print(Student_name)

Student_name[0] = "SHEKHAR SUMAN"
print(Student_name)

# immutable means can'nt changeable the value

#   For Example : 

name = "Shekhar"
print(name[4])
name[4] = "H" 
print(name[4])

