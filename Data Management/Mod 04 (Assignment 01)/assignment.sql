-- Assignment 01 --
-- -- -- -- -- -- -- -- -- --
create database ASSIGNMENT_01;

use ASSIGNMENT_01;

create table
    STUDENT (
        ROLL varchar(10) primary key,
        NAME varchar(25) not null,
        CLASS varchar(15),
        SECTION char(2),
        PHONE varchar(12),
        ADDRESS varchar(40)
    );

insert into
    STUDENT (ROLL, NAME, CLASS, SECTION, PHONE, ADDRESS)
values
    (1, 'Sadia', '12', 'A', '017', 'Dhaka'),
    (
        '20-28991-1',
        'Afrin',
        'BSC 1st year',
        'C4',
        '016',
        'Rajshahi'
    ),
    (
        '20-24971-1',
        'Trina',
        'BSC 3rd year',
        'B2',
        '019',
        'Sylhet'
    );

create table
    LIBRARY (
        BOOK_TITLE varchar(100),
        AUTHOR varchar(20),
        STUDENT_ID varchar(10),
        constraint STUDENT_ID_IS_FK foreign key (STUDENT_ID) references STUDENT (ROLL)
    );

insert into
    LIBRARY (BOOK_TITLE, AUTHOR, STUDENT_ID)
values
    (
        'The C++ Programming Language',
        'Bjarne Stroustrup',
        '20-24971-1'
    ),
    ('Gone with the Wind', 'Margaret Mitchell', '1'),
    (
        'Introduction to Electrodynamics',
        'Pearson',
        '20-24971-1'
    );

select
    *
from
    LIBRARY
where
    STUDENT_ID = '20-24971-1';

create table
    FEES (
        STUDENT_ID varchar(10),
        AMOUNT_PAID double,
        CURRENT_STATUS varchar(10),
        constraint STUDENT_ID_IS_FK_OF_STUDENT_ROLL foreign key (STUDENT_ID) references STUDENT (ROLL)
    );

insert into
    FEES (STUDENT_ID, AMOUNT_PAID, CURRENT_STATUS)
values
    ('20-24971-1', '2500', 'Full Paid'),
    ('1', '720', 'Full Paid'),
    ('20-28991-1', '0', 'Full Paid');

select
    AMOUNT_PAID
from
    FEES
where
    STUDENT_ID = '1';

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

create database EMPLOYEE;

use EMPLOYEE;

create table
    EMPLOYEE (
        EMPLOYEE_ID int,
        FIRST_NAME varchar(15),
        LAST_NAME varchar(20),
        AGE int,
        DEPARTMENT varchar(25)
    );

insert into
    EMPLOYEE (
        EMPLOYEE_ID,
        FIRST_NAME,
        LAST_NAME,
        AGE,
        DEPARTMENT
    )
values
    (1, 'John', 'Doe', 28, 'Sales'),
    (2, 'Jane', 'Smith', 32, 'Marketing'),
    (3, 'Michael', 'Johnson', 35, 'Finance'),
    (4, 'Sarah', 'Brown', 30, 'HR'),
    (5, 'William', 'Davis', 25, 'Engineering'),
    (6, 'Emily', 'Wilson', 28, 'Sales'),
    (7, 'Robert', 'Lee', 33, 'Marketing'),
    (8, 'Laura', 'Hall', 29, 'Finance'),
    (9, 'Thomas', 'White', 31, 'HR'),
    (10, 'Olivia', 'Clark', 27, 'Engineering');

select distinct
    DEPARTMENT
from
    EMPLOYEE;

select
    LAST_NAME
from
    EMPLOYEE
order by
    AGE desc;

select
    LAST_NAME
from
    EMPLOYEE
where
    (
        AGE > 30
        and DEPARTMENT = 'Marketing'
    );

select
    *
from
    EMPLOYEE;

select
    *
from
    EMPLOYEE
where
    FIRST_NAME like '%son%'
    or LAST_NAME like '%son%';

select
    *
from
    EMPLOYEE
where
    DEPARTMENT = 'Engineering';

-- End of Assignment 01 --
-- -- -- -- -- -- -- -- -- --