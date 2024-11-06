# Person class

class Person:
    
    # Constructor to initialize the first and last name
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    # Method to return the full name
    def full_name(self):
        return f"{self.first} {self.last}"
    
    # String representation of the object
    def __str__(self):
        return self.full_name()
    

# Create an instance of the Person class
per1 = Person("James", "White")

# Print the last name of the person
print(per1.last)

# Print the full name of the person using the full_name method
print(per1.full_name())

# Change the last name of the person
per1.last = "Green"

# Print the string representation of the person (which is the full name)
print(per1)