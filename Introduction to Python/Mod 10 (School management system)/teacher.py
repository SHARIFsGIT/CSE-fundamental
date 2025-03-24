import random
from person import Person

class Teacher(Person):
    """
    Class representing a teacher in the school management system.
    Inherits from Person class.
    
    Attributes:
        name (str): Name of the teacher (inherited from Person)
        subject_expertise (list): List of subjects the teacher specializes in
        years_of_experience (int): Years of teaching experience
    """
    
    def __init__(self, name, subject_expertise=None, years_of_experience=0):
        """
        Initialize a Teacher object.
        
        Args:
            name (str): Name of the teacher
            subject_expertise (list, optional): List of subjects the teacher specializes in
            years_of_experience (int, optional): Years of teaching experience
        """
        super().__init__(name)
        self.subject_expertise = subject_expertise if subject_expertise else []
        self.years_of_experience = years_of_experience
    
    def teach(self):
        """Placeholder method for teaching."""
        return f"Teacher {self.name} is teaching"
    
    def evaluate_exam(self, max_marks=100):
        """
        Evaluates exams and returns random marks.
        
        Args:
            max_marks (int, optional): Maximum marks for the exam
            
        Returns:
            int: Random marks between 0 and max_marks
        """
        return random.randint(0, max_marks)
    
    def add_subject_expertise(self, subject):
        """
        Add a subject to teacher's expertise.
        
        Args:
            subject (str): Subject to add to expertise
        """
        if subject not in self.subject_expertise:
            self.subject_expertise.append(subject)
    
    def __str__(self):
        """String representation of the Teacher."""
        expertise = ", ".join(self.subject_expertise) if self.subject_expertise else "None"
        return f"Teacher: {self.name}, Expertise: {expertise}, Experience: {self.years_of_experience} years"