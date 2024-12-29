class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def __str__(self):
        return self.full_name()
    
class Student(Person):
    def __init__(self, first, last, gpa):
        super().__init__(first, last)
        self.gpa = gpa
        
    def __str__(self):
        return f"Student {super().__str__()}\n -- GPA: {self.gpa}"
    
per1 = Person("Cagri", "Efe")
print(per1)
stu1 = Student("Sen","Ben", 3.12)
print(stu1)

class PersonWithProperty:
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def full_name(self):
        return f"{self.first} {self.last}"
    
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
        
    def __str__(self):
        return self.full_name
    
class StudentWithProperty(PersonWithProperty):
    def __init__(self, first, last, gpa):
        super().__init__(first, last)
        self.gpa = gpa
    
    def __str__(self):
        return f"Student: {super().__str__()}\n -- GPA: {self.gpa}"
    
per2 = StudentWithProperty("Alice","White", 2.8)
print(per2.full_name)
print(per2)
        