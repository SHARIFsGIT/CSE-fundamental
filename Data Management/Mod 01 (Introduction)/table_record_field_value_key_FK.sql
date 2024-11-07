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