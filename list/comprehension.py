# List comprehension provides a compact way to create a list from user input. Combines a loop and input() into a single line for it be concise and quick.

user_input = int(input("Enter the number: "))

a = [input(f"Enter the element {i+1}: ") for i in range(user_input)]

print(a)