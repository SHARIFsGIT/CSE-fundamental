class Student:
    def __init__(self, name, studies, id):
        self.name = name
        self.studies = studies
        self.id = id

    def __repr__(self) -> str:
        return f'Student with name: {self.name}, studies: {self.studies}, id: {self.id}'
    
class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher with name: {self.name}, subject: {self.subject}'
    
class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee > 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'Student {name} enrolled with {id} id and get back {fee - 6500}$'
        
    def __repr__(self) -> str:
        print('Welcome to', self.name)

        print('--------- OUR TEACHERS ---------')
        for teacher in self.teachers:
            print(teacher)

        print('--------- OUR STUDENTS ---------')
        for student in self.students:
            print(student)
        return 'All Finished'


# name1 = Student('Shariful', 12, 1)
# print(name1)

# name2 = Teacher('Sayang', 'Math', 101)
# print(name2)

school = School('ABC School')
school.enroll('Sharif', 5200)
school.enroll('Sayang', 8000)

school.add_teacher('Safira', 'Math')
school.add_teacher('Tanju', 'CSE')

print(school)