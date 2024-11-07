-- ProgrammingHero DB --
-- -- -- -- -- -- -- -- -- --
create database ProgrammingHero;

use ProgrammingHero;

create table
    Student (
        Roll char(4) primary key,
        Name varchar(50),
        Marks double
    );

insert into
    Student (Roll, Name, Marks)
values
    (1, 'Shariful', 90);

insert into
    Student (Roll, Name)
values
    (2, 'Safira');

set
    sql_safe_updates = 0;

update Student
set
    Name = 'Shariful Islam'
where
    Roll = 1;

set
    sql_safe_updates = 1;

set
    sql_safe_updates = 0;

delete from Student
where
    Roll = 1;

set
    sql_safe_updates = 1;

drop table Student;

-- End of ProgrammingHero --
-- -- -- -- -- -- -- -- -- --
-- Constraints DB --
-- -- -- -- -- -- -- -- -- --
create database Constraints;

use Constraints;

create table
    Student (
        Roll char(4) primary key,
        Name varchar(50) not null,
        Email varchar(60) unique,
        Address varchar(250),
        Age int check (Age > 10)
    );

insert into
    Student (Roll, Name, Email, Address, Age)
values
    (
        '0001',
        'Shariful',
        'sharifaiub15@gmail.com',
        'Bremen',
        20
    );

insert into
    Student (Roll, Name, Email, Address, Age)
values
    (
        '0002',
        'Shariful',
        'mdsharif@uni-bremen.de',
        'Bremen',
        12
    );

insert into
    Student (Roll, Name, Email, Age)
values
    (
        '0003',
        'Shariful',
        'sharifulislam18@ymail.com',
        30
    );

/*
create table Student(
Roll char(4),
Name varchar(50) not null,
Email varchar(60),
Address varchar(250),
Age int,

primary key (Roll),
unique (Email),
check (Age > 10)
);

create table Student(
Roll char(4),
Name varchar(50) not null,
Email varchar(60),
Address varchar(250),
Age int,

constraint primary key (Roll),
constraint unique (Email),
constraint check (Age > 10)
);

create table Student(
Roll char(4),
Name varchar(50) not null,
Email varchar(60),
Address varchar(250),
Age int,

constraint pk_rule primary key (Roll),
constraint unique_rule unique (Email),
constraint checking_rule check (Age > 10)
);
 */
create table
    Library (
        BookName varcharacter (100),
        -- Roll char(4) --
        Hired char(4),
        -- foreign key (Hired) references Student(Roll) --
        constraint adding_fk foreign key (Hired) references Student (Roll)
    );

create table
    Courses (
        CourseName varchar(20),
        University varchar(30),
        Credit int,
        -- primary key (CourseName, University) --
        -- constraint primary key (CourseName, University) --
        constraint composit_pk primary key (CourseName, University)
    );

-- End of Constraints --
-- -- -- -- -- -- -- -- -- --
-- Select Query --
-- -- -- -- -- -- -- -- -- --
select
    *
from
    Student;

select
    Email
from
    Student;

select
    Roll + Age
from
    Student;

select
    Roll + Age
from
    Student
where
    Roll = 1;

select
    Roll + Age
from
    Student
where
    Roll = '0002';

select
    *
from
    Student
where
    Age >= 20;

select
    *
from
    Student
where
    Age <> 20;

select
    Email
from
    Student
where
    Age >= 30
    and Address = 'Bremen';

select
    *
from
    Student
where
    Age > 30
    or (
        Address = 'Bremen'
        and Roll > 1
    );

/*
select
from
where
order by
limit
offset
 */
select distinct
    Email
from
    Student;

select distinct
    Name
from
    Student;

select
    Email
from
    Student
order by
    Roll asc;

select
    Email
from
    Student
order by
    Roll desc;

select
    *
from
    Student
where
    Age <= 30
limit
    1
offset
    2;

select
    Address
from
    Student
where
    Age <= 30
limit
    2, 1;

select
    Roll
from
    Student
where
    Roll in (1, 2);

select
    Roll
from
    Student
where
    Roll not in (1, 2);

select
    Roll
from
    Student
where
    Email like '%md%';

select
    Age as Job_Experience
from
    Student
where
    Email like '%md%';

-- End of Select Query --
-- -- -- -- -- -- -- -- -- --