
# Time left off last time: 23:21

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # This grade is between 0 - 100
    
    def get_grade(self):
        return self.grade
        
# You could add more functions if you want

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)                  # Wait hold on, figure this logic out before moving forward next time.
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)
###################################################################################

# Actual code starting here

# Define students and courses
s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course1 = Course("Science", 2)

# Adding students to my science course
course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)
print(course1.students[0].name)

myavg = course1.get_average_grade()
print(myavg)