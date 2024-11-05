list1 = ["A", "B", "C", "D"]

print(f"list has {len(list1)} items.")

list2 = ["Red", 17, False, "Python"]
print(list2[0:2]) # ['Red', 17]
print(list2[1:3]) # [17, False]
print(list2[:2]) # ['Red', 17]
print(list2[2:]) # [False, 'Python']
print(list2[-1]) # Python
print(list2[-2]) # False
print(list2[0:-1]) # ['Red', 17, False]

list2[3] = 6
print(list2) # ['Red', 17, False, 6]

list2.append("Apple") # ['Red', 17, False, 6, 'Apple']
list2.insert(3, True) # ['Red', 17, False, True, 6, 'Apple']
list2.remove("Red") # [17, False, True, 6, 'Apple']
print(list2) # [17, False, True, 6, 'Apple']

for i in list2:
    print(i)
    

print("\nCheck if 20 exist in the list:")
if 20 in list2:
    print("Found")
else:
    print("Not found")

list3 = list2.copy()
print(list3) # [17, False, True, 6, 'Apple']