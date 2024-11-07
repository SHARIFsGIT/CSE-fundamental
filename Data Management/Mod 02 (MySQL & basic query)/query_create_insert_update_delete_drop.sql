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