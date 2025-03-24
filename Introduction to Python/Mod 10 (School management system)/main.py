"""
School Management System

This script is the main entry point for the School Management System.
It demonstrates the usage of the classes defined in the system.
"""

from school import School
from classroom import ClassRoom
from subject import Subject
from teacher import Teacher
from student import Student
from person import Person

def main():
    """Main function to demonstrate the School Management System."""
    print("Welcome to the School Management System!")
    print("-" * 50)
    
    # Create a school
    school = School("Sunshine High School", "123 Education Street, Knowledge City")
    school.set_founded_year(1985)
    
    # Set school principal
    principal = Person("Dr. Emma Johnson")
    school.set_principal(principal)
    
    # Add school events
    school.add_school_event("Annual Sports Day", "2023-05-15", "Various sports competitions")
    school.add_school_event("Science Fair", "2023-06-10", "Students showcase science projects")
    
    # Create classrooms
    class_10a = ClassRoom("10-A")
    class_10b = ClassRoom("10-B")
    class_11a = ClassRoom("11-A")
    
    # Add classrooms to school
    school.add_classroom(class_10a)
    school.add_classroom(class_10b)
    school.add_classroom(class_11a)
    
    # Create teachers
    math_teacher = Teacher("Mr. Robert Smith", ["Mathematics"], 8)
    english_teacher = Teacher("Ms. Sarah Wilson", ["English"], 5)
    science_teacher = Teacher("Dr. James Brown", ["Physics", "Chemistry"], 10)
    history_teacher = Teacher("Mrs. Patricia Davis", ["History"], 7)
    
    # Set class teachers
    class_10a.set_class_teacher(math_teacher)
    class_10b.set_class_teacher(english_teacher)
    class_11a.set_class_teacher(science_teacher)
    
    # Create subjects
    math = Subject("Mathematics", math_teacher, 100, 40)
    english = Subject("English", english_teacher, 100, 40)
    physics = Subject("Physics", science_teacher, 100, 40)
    chemistry = Subject("Chemistry", science_teacher, 100, 40)
    history = Subject("History", history_teacher, 100, 40)
    
    # Add syllabus to subjects
    math.add_syllabus_topic("Algebra")
    math.add_syllabus_topic("Geometry")
    math.add_syllabus_topic("Trigonometry")
    
    english.add_syllabus_topic("Grammar")
    english.add_syllabus_topic("Literature")
    english.add_syllabus_topic("Essay Writing")
    
    # Add subjects to classrooms
    class_10a.add_subject(math)
    class_10a.add_subject(english)
    class_10a.add_subject(history)
    
    class_10b.add_subject(math)
    class_10b.add_subject(english)
    class_10b.add_subject(history)
    
    class_11a.add_subject(math)
    class_11a.add_subject(physics)
    class_11a.add_subject(chemistry)
    
    # Add teachers to school
    school.add_teacher("Mathematics", math_teacher)
    school.add_teacher("English", english_teacher)
    school.add_teacher("Physics", science_teacher)
    school.add_teacher("Chemistry", science_teacher)
    school.add_teacher("History", history_teacher)
    
    # Create students
    student1 = Student("John Doe")
    student2 = Student("Jane Smith")
    student3 = Student("Mike Johnson")
    student4 = Student("Emily Davis")
    student5 = Student("David Wilson")
    student6 = Student("Sarah Thompson")
    
    # Admit students to classrooms
    school.student_admission(student1, "10-A")
    school.student_admission(student2, "10-A")
    school.student_admission(student3, "10-B")
    school.student_admission(student4, "10-B")
    school.student_admission(student5, "11-A")
    school.student_admission(student6, "11-A")
    
    # Record attendance for students
    student1.record_attendance("2023-03-01", "present")
    student1.record_attendance("2023-03-02", "present")
    student1.record_attendance("2023-03-03", "absent")
    
    student2.record_attendance("2023-03-01", "present")
    student2.record_attendance("2023-03-02", "absent")
    student2.record_attendance("2023-03-03", "present")
    
    # Conduct semester finals for each classroom
    print("\nConducting semester finals...")
    class_10a.take_semester_final()
    class_10b.take_semester_final()
    class_11a.take_semester_final()
    
    # Display student marks and grades
    print("\nStudent Performance Report:")
    print("-" * 50)
    for student in school.get_all_students():
        print(f"Student: {student.name} (ID: {student.id})")
        print(f"Classroom: {student.classroom}")
        print("Subject Marks:")
        for subject, marks in student.marks.items():
            grade = student.subject_grade.get(subject, "N/A")
            print(f"  {subject}: {marks} - Grade: {grade}")
        print(f"Final Grade: {student.grade}")
        print(f"Attendance: {student.get_attendance_percentage():.1f}%")
        print("-" * 30)
    
    # Generate and display classroom reports
    print("\nClassroom Reports:")
    print("-" * 50)
    for classroom_name, classroom in school.classrooms.items():
        print(classroom.generate_class_report())
        print("-" * 30)
    
    # Generate and display school report
    print("\nSchool Report:")
    print("-" * 50)
    print(school.generate_school_report())

if __name__ == "__main__":
    main()