list = [2, 3, 55, 89]

list.append(323) # adds one element at the end [2, 3, 55, 89, 323]
print(list)

list.sort() #sorts in ascending order 
print(list)

list.sort(reverse=True) # sorts in decending order
print(list)

list.insert(2, 66) # insert element at index 
print(list)

list.reverse()
print(list)

# REMOVE METHOD 
list.remove(3) # Remove the first occorance from the list of element
print(list)

# Pop method
list.pop(2) # Permanent delete the element from the index
print(list)