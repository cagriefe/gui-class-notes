tuple1 = ("A", "B", "C")
print(tuple1)
print(tuple1[0:-1]) # ('A', 'B')
# tuple1[0] = "X" # Error since tuples are immutable

list1 = list(tuple1) # Convert tuple to list for modification
list1[0] = "X"
tuple1 = tuple(list1) # Convert list to tuple again after modification
print(tuple1)

i = 0
while i < len(tuple1):
    print(tuple1[i])
    i += 1
print("Done")

for x in range(5):
    print(x)
print("Done")

for x in range(0, 5):
    print(x)
print("Done")

for x in range(3, 10, 2):
    print(x)
print("Done")