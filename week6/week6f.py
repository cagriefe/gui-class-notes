# Person and Student classes (setter property)

class Person:

    # Constructor to initialize the first and last name
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Property to return the full name
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    # Making it a setter for the full_name property. 
    # It allows setting the full name by splitting the input string into first and last names.
    # Setter for the full name property
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # String representation of the object
    def __str__(self):
        return self.full_name


class Student(Person):

    # Constructor to initialize the first name, last name, and GPA
    def __init__(self, first, last, gpa):
        # Call the constructor of the parent class (Person)
        super().__init__(first, last)
        self.gpa = gpa

    # String representation of the Student object
    def __str__(self):
        return f"Student: {super().__str__()}\n -- GPA: {self.gpa}"


# Create an instance of the Student class
stu1 = Student("Julia", "Smith", 3.6)

# Use the setter property to change the full name
stu1.full_name = "Olivia Ross"

# Print the string representation of the student
print(stu1)