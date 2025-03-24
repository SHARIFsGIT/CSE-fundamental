class School:
    """
    Class representing a school in the school management system.
    
    Attributes:
        name (str): Name of the school
        address (str): Address of the school
        teachers (dict): Dictionary to store teachers associated with subjects
        classrooms (dict): Dictionary to store classrooms
    """
    
    def __init__(self, name, address):
        """
        Initialize a School object.
        
        Args:
            name (str): Name of the school
            address (str): Address of the school
        """
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}
        self.principal = None  # Additional feature: school principal
        self.founded_year = None  # Additional feature: founding year
        self.school_events = []  # Additional feature: school events
    
    def add_classroom(self, classroom):
        """
        Adds a classroom to the school.
        
        Args:
            classroom (ClassRoom): ClassRoom object to add
        """
        self.classrooms[classroom.name] = classroom
    
    def add_teacher(self, subject, teacher):
        """
        Adds a teacher to a specific subject.
        
        Args:
            subject (str): Subject name
            teacher (Teacher): Teacher object to add
        """
        self.teachers[subject] = teacher
        teacher.add_subject_expertise(subject)
    
    def student_admission(self, student, classroom_name):
        """
        Enrolls a student into a classroom.
        
        Args:
            student (Student): Student object to enroll
            classroom_name (str): Name of the classroom to enroll into
            
        Returns:
            bool: True if admission is successful, False otherwise
        """
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_student(student)
            return True
        return False
    
    @staticmethod
    def calculate_grade(marks):
        """
        Static method to calculate grade based on marks.
        
        Args:
            marks (int): Marks to calculate grade for
            
        Returns:
            str: Grade corresponding to the marks
        """
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"
    
    @staticmethod
    def grade_to_value(grade):
        """
        Static method to convert grade to its corresponding value.
        
        Args:
            grade (str): Grade to convert
            
        Returns:
            int: Value corresponding to the grade
        """
        grade_value = {
            "A+": 5, "A": 4, "B": 3, "C": 2, "D": 1, "F": 0, "N/A": -1
        }
        return grade_value.get(grade, -1)
    
    @staticmethod
    def value_to_grade(value):
        """
        Static method to convert value to its corresponding grade.
        
        Args:
            value (int): Value to convert
            
        Returns:
            str: Grade corresponding to the value
        """
        value_grade = {
            5: "A+", 4: "A", 3: "B", 2: "C", 1: "D", 0: "F", -1: "N/A"
        }
        return value_grade.get(value, "N/A")
    
    def set_principal(self, principal):
        """
        Set the school principal.
        
        Args:
            principal (Person): Person object to set as principal
        """
        self.principal = principal
    
    def set_founded_year(self, year):
        """
        Set the founding year of the school.
        
        Args:
            year (int): Founding year
        """
        self.founded_year = year
    
    def add_school_event(self, event_name, event_date, description=""):
        """
        Add a school event.
        
        Args:
            event_name (str): Name of the event
            event_date (str): Date of the event
            description (str, optional): Description of the event
        """
        self.school_events.append({
            "name": event_name,
            "date": event_date,
            "description": description
        })
    
    def get_all_students(self):
        """
        Get all students in the school.
        
        Returns:
            list: List of all Student objects in the school
        """
        all_students = []
        for classroom in self.classrooms.values():
            all_students.extend(classroom.students)
        return all_students
    
    def generate_school_report(self):
        """
        Generate a comprehensive school report.
        
        Returns:
            str: School report
        """
        report = f"SCHOOL REPORT: {self.name}\n"
        report += f"Address: {self.address}\n"
        
        if self.founded_year:
            report += f"Founded: {self.founded_year}\n"
        
        if self.principal:
            report += f"Principal: {self.principal.name}\n"
        
        report += f"Number of classrooms: {len(self.classrooms)}\n"
        report += f"Number of teachers: {len(self.teachers)}\n"
        
        total_students = len(self.get_all_students())
        report += f"Total students: {total_students}\n"
        
        # Add classroom-wise stats
        report += "\nClassroom Statistics:\n"
        for name, classroom in self.classrooms.items():
            report += f"  {name}: {len(classroom.students)} students\n"
        
        # Add upcoming events
        if self.school_events:
            report += "\nUpcoming Events:\n"
            for event in self.school_events:
                report += f"  {event['name']} - {event['date']}\n"
        
        return report
    
    def __repr__(self):
        """
        String representation of the school, including classroom details and student exam marks.
        
        Returns:
            str: Detailed representation of the school
        """
        repr_str = f"School: {self.name}\nAddress: {self.address}\n\n"
        
        # Add classroom details
        repr_str += "Classrooms:\n"
        for name, classroom in self.classrooms.items():
            repr_str += f"  {name}: {len(classroom.students)} students, "
            repr_str += f"{len(classroom.subjects)} subjects\n"
            
            # Add student details for each classroom
            if classroom.students:
                repr_str += "    Students:\n"
                for student in classroom.students:
                    repr_str += f"      - {student.name} (ID: {student.id})\n"
                    
                    # Add subject marks if available
                    if student.marks:
                        repr_str += "        Marks:\n"
                        for subject, marks in student.marks.items():
                            repr_str += f"          {subject}: {marks}\n"
        
        return repr_str