-- Foreign key on delete operation --
create table
    STUDENT (ROLL varchar(5) primary key, NAME varchar(20));

create table
    COURSE (
        COURSE_NO varchar(5) primary key,
        COURSE_NAME varchar(20)
    );

create table
    ENROLL (
        ROLL varchar(5),
        COURSE_NO varchar(5),
        DATE date,
        -- all entry will be deleted, not only the recent one --
        foreign key (ROLL) references STUDENT (ROLL) on delete cascade,
        foreign key (COURSE_NO) references COURSE (COURSE_NO) on delete cascade,
        -- if i dont want to delete but want to set null on the deleted data --
        foreign key (ROLL) references STUDENT (ROLL) on delete set null,
        foreign key (COURSE_NO) references COURSE (COURSE_NO) on delete set null
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- Set operation --
-- 01. UNION		: all unique values
select
    *
from
    EMPLOYEES
where
    SALARY > 10000
union
select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = 100;

-- 02. UNION ALL	: can have duplicate values
select
    *
from
    EMPLOYEES
where
    SALARY > 10000
union all
select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = 100;

-- 03. INTERSECTION	: only common
select
    *
from
    EMPLOYEES
where
    SALARY > 10000
intersect
select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = 100;

-- 04. MINUS		: remaining values from the 1st set
select
    *
from
    EMPLOYEES
where
    SALARY > 10000
    and DEPARTMENT_ID != 100;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 