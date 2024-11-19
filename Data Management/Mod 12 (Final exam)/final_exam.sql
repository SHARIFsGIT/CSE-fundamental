CREATE DATABASE final_exam;

USE final_exam;

CREATE TABLE
    Instructor (
        InstructorID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL UNIQUE,
        Phone VARCHAR(15),
        Department VARCHAR(50)
    );

CREATE TABLE
    Course (
        CourseID INT AUTO_INCREMENT PRIMARY KEY,
        Title VARCHAR(255) NOT NULL,
        Credits INT NOT NULL,
        InstructorID INT,
        FOREIGN KEY (InstructorID) REFERENCES Instructor (InstructorID)
    );

CREATE TABLE
    Student (
        StudentID INT AUTO_INCREMENT PRIMARY KEY,
        Name VARCHAR(255) NOT NULL,
        Email VARCHAR(255) NOT NULL UNIQUE,
        Phone VARCHAR(15)
    );

CREATE TABLE
    Enrollment (
        EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
        StudentID INT,
        CourseID INT,
        EnrollmentDate DATE NOT NULL,
        FOREIGN KEY (StudentID) REFERENCES Student (StudentID),
        FOREIGN KEY (CourseID) REFERENCES Course (CourseID)
    );

INSERT INTO
    Instructor (Name, Email, Phone, Department)
VALUES
    (
        'Dr. John Smith',
        'john.smith@university.edu',
        '555-1234',
        'Computer Science'
    ),
    (
        'Dr. Alice Johnson',
        'alice.johnson@university.edu',
        '555-5678',
        'Mathematics'
    ),
    (
        'Dr. Robert Brown',
        'robert.brown@university.edu',
        '555-8765',
        'Physics'
    ),
    (
        'Dr. Emma Wilson',
        'emma.wilson@university.edu',
        '555-4321',
        'Biology'
    );

INSERT INTO
    Course (Title, Credits, InstructorID)
VALUES
    ('Introduction to Programming', 3, 1),
    ('Calculus I', 4, 2),
    ('Physics 101', 3, 3),
    ('Biology Basics', 2, 4),
    ('Data Structures', 3, 1);

INSERT INTO
    Student (Name, Email, Phone)
VALUES
    (
        'Michael Scott',
        'michael.scott@students.edu',
        '555-1111'
    ),
    (
        'Pam Beesly',
        'pam.beesly@students.edu',
        '555-2222'
    ),
    (
        'Jim Halpert',
        'jim.halpert@students.edu',
        '555-3333'
    ),
    (
        'Dwight Schrute',
        'dwight.schrute@students.edu',
        '555-4444'
    ),
    (
        'Angela Martin',
        'angela.martin@students.edu',
        '555-5555'
    );

INSERT INTO
    Enrollment (StudentID, CourseID, EnrollmentDate)
VALUES
    (1, 1, '2024-01-10'),
    (2, 1, '2024-01-11'),
    (3, 2, '2024-01-12'),
    (4, 3, '2024-01-13'),
    (5, 4, '2024-01-14'),
    (1, 5, '2024-01-15'),
    (3, 5, '2024-01-16');

-- 01. Draw an Entity-Relationship (ER) diagram to represent this Online Course Management System schema.
-- 02. Write an SQL query to insert a new enrollment record for a student (e.g., StudentID 5) into the course with the highest credit hours.
INSERT INTO
    Enrollment (StudentID, CourseID, EnrollmentDate)
SELECT
    5,
    CourseID,
    CURDATE ()
FROM
    Course
ORDER BY
    Credits DESC
LIMIT
    1;

-- 03. Write an SQL UPDATE query to assign a new instructor to a course (e.g., CourseID 3) by updating the InstructorID.
UPDATE Course
SET
    InstructorID = 1
WHERE
    CourseID = 3;

-- 04. Write an SQL query to find the names of instructors who teach the most credits (total).
SELECT
    Instructor.Name AS InstructorName
FROM
    Instructor
    JOIN Course ON Instructor.InstructorID = Course.InstructorID
GROUP BY
    Instructor.Name
HAVING
    SUM(Course.Credits) = (
        SELECT
            MAX(TotalCredits)
        FROM
            (
                SELECT
                    SUM(Credits) AS TotalCredits
                FROM
                    Course
                GROUP BY
                    InstructorID
            ) AS SubQuery
    );

-- 05. Write an SQL query to list all students who are enrolled in more than two courses.
SELECT
    Student.StudentID,
    Student.Name,
    COUNT(Enrollment.CourseID) AS CourseCount
FROM
    Student
    JOIN Enrollment ON Student.StudentID = Enrollment.StudentID
GROUP BY
    Student.StudentID,
    Student.Name
HAVING
    COUNT(Enrollment.CourseID) > 2;

-- 06. Design an ER diagram for a simple online retail system that includes entities such as Customers, Products, and Orders. Keep the diagram simple.
-- 07. Explain the difference between GROUP BY and ORDER BY in SQL. Provide an example for each to illustrate.
/*
GROUP BY:
It groups the rows that has the same values in a specific column.
COUNT, SUM, MAX, MIN, AVG operations works after GROUP BY function.
Reduce the number of rows according to the grouping data which we are interested to find.

SELECT 
InstructorID,
COUNT(*) AS TotalCourses
FROM 
Course
GROUP BY 
InstructorID;

ORDER BY:
Sort the rows based on one or more columns, either in ascending or in  descending order.
ASC (by default) and DESC functions works after ORDER BY operation. 
It rearrange the rows according to the ASC or DESC order.

SELECT 
Title
FROM 
Course
ORDER BY 
Title ASC;
 */
-- 08. Given a table Instructor with a Salary column, write an SQL query to find the second-highest salary among instructors.
SELECT DISTINCT
    Salary
FROM
    Instructor
ORDER BY
    Salary DESC
LIMIT
    1
OFFSET
    1;

-- 09. You have two tables, Instructor and Course. Use ON DELETE CASCADE on Course so that all courses are deleted when an instructor is removed.
CREATE TABLE
    Course (
        CourseID INT AUTO_INCREMENT PRIMARY KEY,
        Title VARCHAR(255) NOT NULL,
        Credits INT NOT NULL,
        InstructorID INT,
        FOREIGN KEY (InstructorID) REFERENCES Instructor (InstructorID) ON DELETE CASCADE
    );

-- 10. Describe the most challenging topic you encountered in this course. Explain why it was challenging and how you overcame it.
/*
The course was fantastic overall. The initial classes were very easy-going, but I found the subquery topic a bit challenging when we go through 
that part. However, this issue was solved when I learned about Common Table Expressions (CTEs), which made things much easier and clearer. 
Later, as we delved deeper into the course, I encountered some difficulty with the topic of joins, particularly self-joining. I overcame this 
by practicing more problems on the LeetCode platform. Apart from these challenges, I found all the other topics relatively easy to understand.
 */