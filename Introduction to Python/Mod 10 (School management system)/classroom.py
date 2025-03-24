class ClassRoom:
    """
    Class representing a classroom in the school management system.
    
    Attributes:
        name (str): Name of the classroom
        students (list): List to store students
        subjects (list): List to store subjects taught in the classroom
    """
    
    def __init__(self, name):
        """
        Initialize a ClassRoom object.
        
        Args:
            name (str): Name of the classroom
        """
        self.name = name
        self.students = []
        self.subjects = []
        self.class_teacher = None  # Additional feature: class teacher
    
    def add_student(self, student):
        """
        Adds a student to the classroom.
        
        Args:
            student (Student): Student object to add
        """
        if student not in self.students:
            self.students.append(student)
            student.classroom = self.name
    
    def add_subject(self, subject):
        """
        Adds a subject to the classroom.
        
        Args:
            subject (Subject): Subject object to add
        """
        if subject not in self.subjects:
            self.subjects.append(subject)
    
    def take_semester_final(self):
        """
        Conducts semester final exams for all subjects.
        
        Returns:
            dict: Dictionary mapping subjects to their exam results
        """
        results = {}
        for subject in self.subjects:
            subject_results = subject.exam(self.students)
            results[subject.name] = subject_results
        
        # After exams, calculate final grades for all students
        for student in self.students:
            student.calculate_final_grade()
            student.get_subject_grades()
        
        return results
    
    def get_top_students(self, limit=3):
        """
        Method to sort students by grade.
        
        Args:
            limit (int, optional): Number of top students to return
            
        Returns:
            list: List of top students
        """
        # Ensure all students have calculated grades
        for student in self.students:
            if student.grade is None:
                student.calculate_final_grade()
        
        # Define a grade value mapping for sorting
        grade_value = {
            "A+": 5, "A": 4, "B": 3, "C": 2, "D": 1, "F": 0, "N/A": -1
        }
        
        # Sort students by grade
        sorted_students = sorted(self.students, key=lambda s: grade_value.get(s.grade, -1), reverse=True)
        
        return sorted_students[:limit]
    
    def set_class_teacher(self, teacher):
        """
        Set the class teacher for this classroom.
        
        Args:
            teacher (Teacher): Teacher object to set as class teacher
        """
        self.class_teacher = teacher
    
    def generate_class_report(self):
        """
        Generate a report for the classroom.
        
        Returns:
            str: Class report
        """
        report = f"Class Report for {self.name}\n"
        report += f"Number of students: {len(self.students)}\n"
        report += f"Number of subjects: {len(self.subjects)}\n"
        
        if self.class_teacher:
            report += f"Class Teacher: {self.class_teacher.name}\n"
        
        # Add subject-wise performance
        report += "\nSubject-wise Performance:\n"
        for subject in self.subjects:
            passing_students = sum(1 for student in self.students if student.marks.get(subject.name, 0) >= subject.pass_marks)
            
            pass_percentage = (passing_students / len(self.students)) * 100 if self.students else 0
            
            report += f"  {subject.name}: Pass Rate - {pass_percentage:.2f}%\n"
        
        # Add top students
        top_students = self.get_top_students()
        report += "\nTop Students:\n"
        for i, student in enumerate(top_students, 1):
            report += f"  {i}. {student.name} (Grade: {student.grade})\n"
        
        return report
    
    def __str__(self):
        """String representation of the ClassRoom."""
        return f"Classroom: {self.name}, Students: {len(self.students)}, Subjects: {len(self.subjects)}"