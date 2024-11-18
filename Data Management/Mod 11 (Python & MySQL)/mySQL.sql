create database STUDENT_LIBRARY_MANAGEMENT;

use STUDENT_LIBRARY_MANAGEMENT;

create table STUDENT
(
	ROLL varchar(4) primary key,
    NAME varchar(25)
);

create table LIBRARIAN
(
	LIB_ID varchar(4) primary key,
    LIB_NAME varchar(25)
);

create table BOOK
(
	BOOK_ID varchar(4) primary key,
    BOOK_NAME varchar(25),
    BOOK_GENRE varchar(25)
);

create table BORROW
(
	WHO_BORROWED_ROLL varchar(4),
    WHICH_BOOK_ID varchar(4),
    
	BORROW_DATE date,
    RETURN_DATE date,
    
    foreign key (WHO_BORROWED_ROLL) references STUDENT(ROLL),
    foreign key (WHICH_BOOK_ID) references BOOK(BOOK_ID),
    
    primary key(WHO_BORROWED_ROLL, WHICH_BOOK_ID)
);

create table PERMISSION
(
    WHICH_BOOK_ID varchar(4),
    WHO_PERMITTED_LIB_ID varchar(4),
    
    foreign key (WHICH_BOOK_ID) references BOOK(BOOK_ID),
    foreign key (WHO_PERMITTED_LIB_ID) references LIBRARIAN(LIB_ID),
    
    primary key(WHICH_BOOK_ID, WHO_PERMITTED_LIB_ID)
);


                        -- Module 11.5 (Practice) --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- 01. What are the types of entity attribute?
/*
1. Simple Attribute --> Example: Name, Age, Gender.
2. Composite Attribute --> Example: Full Name can be divided into First Name and Last Name.
3. Derived Attribute --> Example: Age can be derived from the Date of Birth.
4. Single-Valued Attribute --> Example: A person's Social Security Number.
5. Multi-Valued Attribute --> Example: A person might have multiple Phone Numbers or Email Addresses.
6. Key Attribute --> Example: Student ID or Employee ID.
7. Null Attribute --> Example: Middle Name might be null for people who don't have one.
8. Stored Attribute --> Example: Salary of an employee (these attributes stored directly in the DB and not derived from other attributes)
*/

-- 02. What are the main difference between executing SQL query using python and SQL query in MySQL workbench?
/*
1. Environment

Python
	Code-Based: Queries are executed within a Python script or interactive Python environment.
	Requires a MySQL driver, such as mysql-connector, PyMySQL, or SQLAlchemy, to connect to the database.
	The environment must have the appropriate Python library installed and configured to establish a connection.
MySQL Workbench:
	GUI-Based: Queries are executed directly through a graphical interface provided by MySQL Workbench.
	No coding is required; the interface provides a query editor for writing and running SQL commands.
	Ideal for manual and interactive database exploration.
*/