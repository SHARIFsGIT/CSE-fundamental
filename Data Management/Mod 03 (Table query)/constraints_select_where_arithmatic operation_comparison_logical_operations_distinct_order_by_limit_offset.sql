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