
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
