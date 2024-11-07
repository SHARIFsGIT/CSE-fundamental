select
    *
from
    COUNTRIES;

select
    *
from
    DEPARTMENTS;

select
    *
from
    EMPLOYEES;

select
    FIRST_NAME,
    LAST_NAME
from
    EMPLOYEES;

select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = 60;

select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = 60
    and SALARY > 5000;

select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = 60
    or SALARY > 9000;

select
    FIRST_NAME,
    SALARY,
    SALARY + 10000
from
    EMPLOYEES;

select
    FIRST_NAME,
    SALARY,
    SALARY + 10000
from
    EMPLOYEES
where
    DEPARTMENT_ID = 100;

select
    *
from
    EMPLOYEES
where
    SALARY < 6000;

select distinct
    JOB_ID
from
    EMPLOYEES;

select
    *
from
    EMPLOYEES
order by
    SALARY desc;

select
    *
from
    EMPLOYEES
order by
    SALARY desc
limit
    2;

select
    *
from
    EMPLOYEES
order by
    SALARY desc
limit
    2, 5;

select
    *
from
    EMPLOYEES
order by
    SALARY desc
limit
    2
offset
    5;

select
    *
from
    EMPLOYEES
where
    LAST_NAME like '%GREEN%';

select
    FIRST_NAME,
    SALARY as CURRENT_SALARY,
    SALARY + 10000 as INCREASED_SALARY
from
    EMPLOYEES;

-- Some function also learned --
select
    upper(FIRST_NAME)
from
    EMPLOYEES;

select
    cos(radians (90));

select
    pi ();

select
    round(pi (), 2);

select
    rand ();

-- Group functions --
-- max, min, count, sum, avg --
select
    max(SALARY)
from
    EMPLOYEES;

select
    avg(SALARY)
from
    EMPLOYEES;

select
    count(SALARY)
from
    EMPLOYEES;

select
    count(*)
from
    EMPLOYEES;

-- Show how many rows available --
select
    max(SALARY)
from
    EMPLOYEES
group by
    DEPARTMENT_ID;

select
    DEPARTMENT_ID,
    max(SALARY)
from
    EMPLOYEES
group by
    DEPARTMENT_ID;

select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = 20;

select
    DEPARTMENT_ID,
    avg(SALARY)
from
    EMPLOYEES
group by
    DEPARTMENT_ID;

select
    DEPARTMENT_ID,
    count(*)
from
    EMPLOYEES
group by
    DEPARTMENT_ID;

-- Having: applied on group function --
select
    DEPARTMENT_ID,
    max(SALARY)
from
    EMPLOYEES
where
    DEPARTMENT_ID != 20
group by
    DEPARTMENT_ID;

select
    DEPARTMENT_ID,
    max(SALARY)
from
    EMPLOYEES
where
    DEPARTMENT_ID != 20
group by
    DEPARTMENT_ID
having
    max(SALARY) > 5000;

select
    DEPARTMENT_ID,
    max(SALARY) as SAL
from
    EMPLOYEES
where
    DEPARTMENT_ID != 20
group by
    DEPARTMENT_ID
having
    SAL > 5000;

alter table EMPLOYEES
add column GENDER varchar(50);

alter table EMPLOYEES
drop column GENDER;

alter table EMPLOYEES modify column SALARY int;

alter table EMPLOYEES modify column SALARY decimal;