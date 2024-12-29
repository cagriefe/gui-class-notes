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
# Define the Student class that inherits from Person
class Student(Person):
    # Constructor to initialize the first name, last name, and GPA
    def __init__(self, first, last, gpa):
        # Call the constructor of the parent class (Person)
        super().__init__(first, last)
        self.gpa = gpa
    # String representation of the Student object
    def __str__(self):
        return f"Student: {super().__str__()}\n -- GPA: {self.gpa}"
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
# Create an instance of the Student class
stu1 = Student("Julia", "Smith", 3.6)
# Print the string representation of the student
print(stu1)

# Example of using the @property decorator for full_name
class PersonWithProperty:
    # Constructor to initialize the first and last name
    def __init__(self, first, last):
        self.first = first
        self.last = last    
    # @property: making it a property of the Person class. 
    # It returns the full name of the person by merging 
    # the first and last names.
    # Property to return the full name
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    # Making it a setter for the full_name property. 
    # It allows setting the full name by splitting the 
    # input string into first and last names.
    # Setter for the full name property
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    # String representation of the object
    def __str__(self):
        return self.full_name
# Define the Student class that inherits from PersonWithProperty
class StudentWithProperty(PersonWithProperty):
    # Constructor to initialize the first name, last name, and GPA
    def __init__(self, first, last, gpa):
        # Call the constructor of the parent class (PersonWithProperty)
        super().__init__(first, last)
        self.gpa = gpa
    # String representation of the Student object
    def __str__(self):
        return f"Student: {super().__str__()}\n -- GPA: {self.gpa}"

# Create an instance of the PersonWithProperty class
per2 = PersonWithProperty("Alice", "Brown", 3.6)
# Print the full name of the student using the full_name property
print(per2.full_name)
# Print the string representation of the student
print(per2)


