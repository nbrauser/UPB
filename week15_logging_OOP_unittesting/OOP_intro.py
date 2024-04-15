class Student:
    def __init__(self, first_name, last_name, score):
        self.first_name = first_name
        self.last_name = last_name
        self.email = f'{first_name}.{last_name}@gmail.com'
        self.score = score

    def fullname(self):
        return f'{self.first_name} {self.last_name}'


student1 = Student('Jane', 'Doe', 85)
student2 = Student('John', 'White', 80)
"""
student1.first_name = 'Jane'
student1.last_name = 'Doe'
student1.email = 'Jane.Doe@gmail.com'
student1.score = 85

student2.first_name = 'John'
student2.last_name = 'White'
student2.email = 'John.white@gmail.com'
student2.score = 80
"""
print(student1.email)
print(student2.email)
print(student1.fullname())
print(student2.fullname())