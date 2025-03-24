class Subject:
    """
    Class representing a subject in the school management system.
    
    Attributes:
        name (str): Name of the subject
        teacher (Teacher): Teacher associated with the subject
        max_marks (int): Maximum marks for the subject
        pass_marks (int): Passing marks for the subject
    """
    
    def __init__(self, name, teacher=None, max_marks=100, pass_marks=40):
        """
        Initialize a Subject object.
        
        Args:
            name (str): Name of the subject
            teacher (Teacher, optional): Teacher associated with the subject
            max_marks (int, optional): Maximum marks for the subject
            pass_marks (int, optional): Passing marks for the subject
        """
        self.name = name
        self.teacher = teacher
        self.max_marks = max_marks
        self.pass_marks = pass_marks
        self.syllabus = []  # List to store syllabus topics
    
    def exam(self, students):
        """
        Conducts exam for students and records their marks.
        
        Args:
            students (list): List of Student objects
            
        Returns:
            dict: Dictionary mapping students to their marks
        """
        results = {}
        for student in students:
            if self.teacher:
                marks = self.teacher.evaluate_exam(self.max_marks)
            else:
                # If no teacher is assigned, generate random marks between 0 and max_marks
                import random
                marks = random.randint(0, self.max_marks)
            
            # Record marks for the student
            student.add_marks(self.name, marks)
            results[student] = marks
        
        return results
    
    def add_syllabus_topic(self, topic):
        """
        Add a topic to the syllabus.
        
        Args:
            topic (str): Topic to add to the syllabus
        """
        self.syllabus.append(topic)
    
    def is_passing(self, marks):
        """
        Check if the marks are passing.
        
        Args:
            marks (int): Marks to check
            
        Returns:
            bool: True if marks are passing, False otherwise
        """
        return marks >= self.pass_marks
    
    def __str__(self):
        """String representation of the Subject."""
        teacher_name = self.teacher.name if self.teacher else "Not assigned"
        return f"Subject: {self.name}, Teacher: {teacher_name}, Max Marks: {self.max_marks}, Pass Marks: {self.pass_marks}"