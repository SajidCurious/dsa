# Accessing index and value in list Using enumerate()
# enumerate() is preferred and most efficient method for accessing both index and value in Python. It doesn’t require manual handling of indices.

a = ["Sajid", "Wajid", "Majid"]

for index,value in enumerate(a):
    print(index, value)