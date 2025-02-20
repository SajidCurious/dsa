# Removing Elements from List
# We can remove elements from a list using:

# remove(): Removes the first occurrence of an element.
# pop(): Removes the element at a specific index or the last element if no index is specified.
# del statement: Deletes an element at a specified index.

a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)  
