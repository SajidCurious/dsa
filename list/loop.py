# This method lets users add one element at a time, it is ideal when the size of the list is fixed or predefined. Here we are using a loop to repeatedly take input and append it to the list.

a = []

# Get the number of elements
# n = int(input("Enter the number of elements: "))

# # Append elements to the list
# for i in range(n):
#     element = input(f"Enter element {i+1}: ")
#     a.append(element)

# print("List:", a)

# Example 2
a = []
s = int(input("Enter the number: "))

for i in range(s):
    element = input(f"Enter element {i+1}: ")
    a.append(element)

print("List:", a)
