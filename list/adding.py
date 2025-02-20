# Adding Elements into List
# We can add elements to a list using the following methods:

# append(): Adds an element at the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Adds an element at a specific position.

# Initialize an empty list
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 
