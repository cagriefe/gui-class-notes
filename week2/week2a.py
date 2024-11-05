# Variables
product_name = "Pen"
price = 5
avaliable = True

# Printing variables
print(product_name + " $"+ str(price) + ".")
print(f"{product_name} ${price}.")

# Input
# age = int(input("Enter your age: "))
# age += 1
# print(age)

# Multiple variable assignment
a = b = c = "Hey"
d, e, f = 3 , "A", False

print(a, b, c)
print(d, e, f)
print(type(d))

# User input and conditional statements
num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less than {num2}.")
else:
    print(f"{num1} is equal to {num2}.")