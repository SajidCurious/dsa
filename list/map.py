# If numeric inputs are needed we can use map() to convert them to integers. Wrap map() in list() to store the result as a list

# Get user input, split it, and convert to integers
# user_input = list(map(int, input("Enter numbers separated by space: ").split()))

# print("List:", user_input)

# Example 2
user_input = list(map(int, input("Enter the number separated by the spaces: ").split()))

print(user_input)