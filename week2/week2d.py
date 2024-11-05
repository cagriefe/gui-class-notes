current_year = 2024


def calculate_age(birth_year):
    return current_year - int(birth_year)

age = calculate_age(2003)
print(f"Age is {age}")

def print_age(birth_year):
    return print(f"Your age is {calculate_age(birth_year)}")

print_age(2003)