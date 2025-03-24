from person import Person

class Student(Person):
    """
    Class representing a student in the school management system.
    Inherits from Person class.
    
    Attributes:
        name (str): Name of the student (inherited from Person)
        classroom (str): Classroom the student is enrolled in
        marks (dict): Dictionary to store marks obtained in subjects
        subject_grade (dict): Dictionary to store grades obtained in subjects
        grade (str): Final grade of the student
        _id (int): Student ID (private attribute with getter and setter)
    """
    
    # Class variable to keep track of student IDs
    _next_id = 1000
    
    def __init__(self, name, classroom=None):
        """
        Initialize a Student object.
        
        Args:
            name (str): Name of the student
            classroom (str, optional): Classroom the student is enrolled in
        """
        super().__init__(name)
        self.classroom = classroom
        self.marks = {}
        self.subject_grade = {}
        self.grade = None
        self._id = Student._next_id
        Student._next_id += 1
        self.attendance = {}  # Track attendance by date
    
    @property
    def id(self):
        """Getter for student ID."""
        return self._id
    
    @id.setter
    def id(self, value):
        """Setter for student ID."""
        if isinstance(value, int) and value > 0:
            self._id = value
        else:
            raise ValueError("Student ID must be a positive integer")
    
    def add_marks(self, subject, marks):
        """
        Add marks for a subject.
        
        Args:
            subject (str): Subject name
            marks (int): Marks obtained in the subject
        """
        self.marks[subject] = marks
    
    def calculate_final_grade(self):
        """
        Calculate the final grade of the student based on average marks.
        
        Returns:
            str: Final grade of the student
        """
        if not self.marks:
            self.grade = "N/A"
            return self.grade
        
        # Calculate average marks
        total_marks = sum(self.marks.values())
        average_marks = total_marks / len(self.marks)
        
        # Assign grade based on average marks
        if average_marks >= 90:
            grade = "A+"
        elif average_marks >= 80:
            grade = "A"
        elif average_marks >= 70:
            grade = "B"
        elif average_marks >= 60:
            grade = "C"
        elif average_marks >= 50:
            grade = "D"
        else:
            grade = "F"
        
        self.grade = grade
        return grade
    
    def get_subject_grades(self):
        """
        Calculate grades for each subject.
        """
        for subject, marks in self.marks.items():
            if marks >= 90:
                self.subject_grade[subject] = "A+"
            elif marks >= 80:
                self.subject_grade[subject] = "A"
            elif marks >= 70:
                self.subject_grade[subject] = "B"
            elif marks >= 60:
                self.subject_grade[subject] = "C"
            elif marks >= 50:
                self.subject_grade[subject] = "D"
            else:
                self.subject_grade[subject] = "F"
    
    def record_attendance(self, date, status):
        """
        Record attendance for a given date.
        
        Args:
            date (str): Date in string format (e.g., '2023-01-10')
            status (str): Attendance status ('present', 'absent', 'late')
        """
        self.attendance[date] = status
    
    def get_attendance_percentage(self):
        """
        Calculate attendance percentage.
        
        Returns:
            float: Attendance percentage
        """
        if not self.attendance:
            return 0.0
            
        present_count = sum(1 for status in self.attendance.values() if status == 'present')
        return (present_count / len(self.attendance)) * 100
    
    def __str__(self):
        """String representation of the Student."""
        return f"Student ID: {self._id}, Name: {self.name}, Classroom: {self.classroom}, Grade: {self.grade}"