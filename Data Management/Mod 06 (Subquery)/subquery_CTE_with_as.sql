use DUMMYDB;

select
    *
from
    EMPLOYEES
where
    FIRST_NAME = 'PETER';

select
    *
from
    EMPLOYEES
where
    EMPLOYEE_ID = 144;

select
    *
from
    EMPLOYEES
where
    SALARY < (
        select
            SALARY
        from
            EMPLOYEES
        where
            EMPLOYEE_ID = 144
    );

select
    max(SALARY)
from
    EMPLOYEES;

select
    *
from
    EMPLOYEES
where
    SALARY = (
        select
            max(SALARY)
        from
            EMPLOYEES
    );

select
    *
from
    DEPARTMENTS;

select
    *
from
    EMPLOYEES;

select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = 20;

select
    DEPARTMENT_ID
from
    DEPARTMENTS
where
    DEPARTMENT_NAME = 'MARKETING';

select
    *
from
    EMPLOYEES
where
    DEPARTMENT_ID = (
        select
            DEPARTMENT_ID
        from
            DEPARTMENTS
        where
            DEPARTMENT_NAME = 'MARKETING'
    );

select
    max(SALARY)
from
    EMPLOYEES
where
    DEPARTMENT_ID = (
        select
            DEPARTMENT_ID
        from
            DEPARTMENTS
        where
            DEPARTMENT_NAME = 'MARKETING'
    );

select
    count(*)
from
    EMPLOYEES
where
    DEPARTMENT_ID = (
        select
            DEPARTMENT_ID
        from
            DEPARTMENTS
        where
            DEPARTMENT_NAME = 'IT'
    );

select
    count(*) as MEMBERS
from
    EMPLOYEES
where
    DEPARTMENT_ID = (
        select
            DEPARTMENT_ID
        from
            DEPARTMENTS
        where
            DEPARTMENT_NAME = 'IT'
    );

select
    *
from
    EMPLOYEES
where
    JOB_ID = (
        select
            JOB_ID
        from
            JOBS
        where
            JOB_TITLE = 'PROGRAMMER'
    );

select
    sum(SALARY)
from
    EMPLOYEES
where
    JOB_ID = (
        select
            JOB_ID
        from
            JOBS
        where
            JOB_TITLE = 'PROGRAMMER'
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- Find the second heighest salary and who got that --
-- Way 01 --
select distinct
    SALARY
from
    EMPLOYEES
order by
    SALARY desc
limit
    1
offset
    1;

select
    *
from
    EMPLOYEES
where
    SALARY = (
        select distinct
            SALARY
        from
            EMPLOYEES
        order by
            SALARY desc
        limit
            1
        offset
            1
    );

-- Way 02 --
select
    max(SALARY)
from
    EMPLOYEES;

select
    max(SALARY)
from
    EMPLOYEES
where
    SALARY < (
        select
            max(SALARY)
        from
            EMPLOYEES
    );

select
    *
from
    EMPLOYEES
where
    SALARY = (
        select
            max(SALARY)
        from
            EMPLOYEES
        where
            SALARY < (
                select
                    max(SALARY)
                from
                    EMPLOYEES
            )
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- Find all employee who have more salary than manager --
select
    *
from
    EMPLOYEES as EMP
where
    SALARY > (
        select
            SALARY
        from
            EMPLOYEES as MGR
        where
            EMP.MANAGER_ID = MGR.EMPLOYEE_ID
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- Employee & manager has same job --
select
    *
from
    EMPLOYEES as EMP
where
    JOB_ID = (
        select
            JOB_ID
        from
            EMPLOYEES as MGR
        where
            EMP.MANAGER_ID = MGR.EMPLOYEE_ID
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

-- Common Table Expression --
select
    *
from
    EMPLOYEES
limit
    5;

with
    TEMP as (
        select
            *
        from
            EMPLOYEES
        limit
            5
    )
select
    *
from
    TEMP;

with
    AVG_IT as (
        select
            avg(SALARY) as IT_SAL
        from
            EMPLOYEES
        where
            DEPARTMENT_ID = 60
    ),
    MAX_MKT as (
        select
            max(SALARY) as MKT_SAL
        from
            EMPLOYEES
        where
            DEPARTMENT_ID = 20
    )
select
    *
from
    EMPLOYEES
where
    SALARY > (
        select
            IT_SAL
        from
            AVG_IT
    )
    and SALARY < (
        select
            MKT_SAL
        from
            MAX_MKT
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- Module 6.5 (Practice) --
-- 1. Who gets third highest salary?
select
    *
from
    EMPLOYEES
where
    SALARY = (
        select distinct
            SALARY
        from
            EMPLOYEES
        order by
            SALARY desc
        limit
            1
        offset
            2
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- 2. Who gets third lowest salary?
select
    *
from
    EMPLOYEES
where
    SALARY = (
        select distinct
            SALARY
        from
            EMPLOYEES
        order by
            SALARY asc
        limit
            1
        offset
            2
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- 3. Which employee has been hired after Steven?
SELECT
    *
FROM
    employees
WHERE
    hire_date = (
        SELECT
            MIN(hire_date)
        FROM
            employees
        WHERE
            hire_date > (
                SELECT
                    hire_date
                FROM
                    employees
                WHERE
                    first_name = 'Steven'
                    AND last_name = 'King'
            )
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- 1. Who gets third lowest salary? (using common table)
WITH
    TEMP AS (
        SELECT DISTINCT
            SALARY
        FROM
            EMPLOYEES
        ORDER BY
            SALARY DESC
        LIMIT
            1
        OFFSET
            2
    )
SELECT
    *
FROM
    EMPLOYEES
WHERE
    SALARY = (
        SELECT
            SALARY
        FROM
            TEMP
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 

-- 2. Who gets third lowest salary?
WITH
    TEMP AS (
        SELECT DISTINCT
            SALARY
        FROM
            EMPLOYEES
        ORDER BY
            SALARY ASC
        LIMIT
            1
        OFFSET
            2
    )
SELECT
    *
FROM
    EMPLOYEES
WHERE
    SALARY = (
        SELECT
            SALARY
        FROM
            TEMP
    );

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 