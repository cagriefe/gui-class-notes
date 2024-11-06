# Person and Student classes (getter property)

class Person:

    # Constructor to initialize the first and last name
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # The full_name method is decorated with @property, making it a property of the Person class. 
    # It returns the full name of the person by concatenating the first and last names.
    # Property to return the full name
    @property
    def full_name(self):
        return f"{self.first} {self.last}"

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

# Print the full name of the student using the full_name property
print(stu1.full_name)

# Print the string representation of the student
print(stu1)