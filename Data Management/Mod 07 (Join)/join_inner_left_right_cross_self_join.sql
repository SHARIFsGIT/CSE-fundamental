-- Join table without join query --
use DUMMYDB;

select
    *
from
    EMPLOYEES;

select
    *
from
    DEPARTMENTS;

select
    FIRST_NAME,
    EMPLOYEES.DEPARTMENT_ID,
    DEPARTMENT_NAME
from
    EMPLOYEES,
    DEPARTMENTS
where
    EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- By using join query --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- Inner join: Common on employee and department --
select
    FIRST_NAME,
    EMPLOYEES.DEPARTMENT_ID,
    DEPARTMENT_NAME
from
    EMPLOYEES
    join DEPARTMENTS on EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID;

-- Or --
select
    FIRST_NAME,
    EMPLOYEES.DEPARTMENT_ID,
    DEPARTMENT_NAME
from
    EMPLOYEES
    inner join DEPARTMENTS using (DEPARTMENT_ID);

-- Employee first name, salary, how less he got from department average salary
select
    EMPLOYEES.FIRST_NAME,
    EMPLOYEES.SALARY,
    (
        select
            avg(SALARY)
        from
            EMPLOYEES
        where
            DEPARTMENT_ID = EMPLOYEES.DEPARTMENT_ID
    ) - EMPLOYEES.SALARY as INCOME
from
    EMPLOYEES
    join DEPARTMENTS on EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID;

-- Show department names whose minimum salary less than 5000
select
    DEPARTMENT_NAME,
    min(SALARY),
    avg(SALARY)
from
    EMPLOYEES
    join DEPARTMENTS on EMPLOYEES.DEPARTMENT_ID = DEPARTMENTS.DEPARTMENT_ID
group by
    DEPARTMENT_NAME
having
    min(SALARY) > 5000;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- Left join: Only employee --
select
    FIRST_NAME,
    EMPLOYEES.DEPARTMENT_ID,
    DEPARTMENT_NAME
from
    EMPLOYEES
    left join DEPARTMENTS using (DEPARTMENT_ID);

-- Show departments where no employees available
SELECT
    DEPARTMENTS.DEPARTMENT_NAME
FROM
    DEPARTMENTS
    LEFT JOIN EMPLOYEES ON DEPARTMENTS.DEPARTMENT_ID = EMPLOYEES.DEPARTMENT_ID
WHERE
    EMPLOYEES.DEPARTMENT_ID IS NULL;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- Right join: Only department --
select
    FIRST_NAME,
    EMPLOYEES.DEPARTMENT_ID,
    DEPARTMENT_NAME
from
    EMPLOYEES
    right join DEPARTMENTS using (DEPARTMENT_ID);

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- Cross join: Takes all (left, common, right) --
select
    FIRST_NAME,
    EMPLOYEES.DEPARTMENT_ID,
    DEPARTMENT_NAME
from
    EMPLOYEES
    cross join DEPARTMENTS using (DEPARTMENT_ID);

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- Self join: Join itself table with different column --
-- Show employee first name and manager name
select
    MAN.FIRST_NAME as EMPLOYEE,
    EMP.FIRST_NAME as MANAGER
from
    EMPLOYEES as EMP
    join EMPLOYEES as MAN on EMP.EMPLOYEE_ID = MAN.MANAGER_ID;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- Module 7.5 (Practice) --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
-- 1. Show the employee names and corresponding job_title without using JOIN query
select
    FIRST_NAME,
    JOB_TITLE
from
    EMPLOYEES,
    JOBS
where
    EMPLOYEES.JOB_ID = JOBS.JOB_ID;

-- 2. Show the employee names and corresponding job_title using JOIN query
select
    FIRST_NAME,
    JOB_TITLE
from
    EMPLOYEES
    inner join JOBS using (JOB_ID);

-- 3. Show the name of the employee and the job_title who receives the maximum salary
select
    FIRST_NAME,
    JOB_TITLE
from
    EMPLOYEES
    join JOBS on EMPLOYEES.JOB_ID = JOBS.JOB_ID
where
    EMPLOYEES.SALARY = (
        select
            max(SALARY)
        from
            EMPLOYEES
    );

-- 4. Show the list of employee names and corresponding manager names
select
    MAN.FIRST_NAME as EMPLOYEE,
    EMP.FIRST_NAME as MANAGER
from
    EMPLOYEES as EMP
    join EMPLOYEES as MAN on EMP.EMPLOYEE_ID = MAN.MANAGER_ID;