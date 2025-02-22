# Using range()
# range() generates an iterator that produces numbers within a specified range. It is highly efficient as it doesn’t create the entire list upfront, making it memory-friendly. Converting the iterator to a list gives us the full range of numbers.

r1 = 0
r2 = 10

li = list(range(r1,r2))

print(li)