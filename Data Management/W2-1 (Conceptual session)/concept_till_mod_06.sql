-- Create Database
CREATE DATABASE test;

USE test;

-- Create Table
CREATE TABLE
    person (
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(50) UNIQUE
    );

-- Insert Records
INSERT INTO
    person (id, name, email)
VALUES
    (1, "Mr. X", "abcd@example.com");

INSERT INTO
    person (id, name, email)
VALUES
    (2, "Mr. X", "xyz@example.com");

-- Alter Table
ALTER TABLE person CHANGE COLUMN email email VARCHAR(100);

ALTER TABLE person
ADD COLUMN address VARCHAR(250);

ALTER TABLE person
DROP COLUMN name;

-- Select Records
SELECT
    *
FROM
    person;

-- Subquery: Find employees who earn more than the average salary
SELECT
    *
FROM
    employees;

SELECT
    AVG(salary) AS average_salary
FROM
    employees;

SELECT
    employee_id,
    first_name,
    last_name,
    salary
FROM
    employees
WHERE
    salary > (
        SELECT
            AVG(salary)
        FROM
            employees
    );

-- Group By & Having: Count the number of employees in each job title
SELECT
    *
FROM
    departments;

SELECT
    job_id,
    COUNT(*) AS count
FROM
    employees
GROUP BY
    job_id
HAVING
    COUNT(*) > 1
ORDER BY
    count DESC;

-- Subquery with Group By: Find departments where the average salary is higher than the overall average salary
SELECT
    department_id,
    (
        SELECT
            department_name
        FROM
            departments
        WHERE
            departments.department_id = employees.department_id
    ) AS department_name,
    AVG(salary) AS average_salary
FROM
    employees
GROUP BY
    department_id
HAVING
    average_salary > (
        SELECT
            AVG(salary)
        FROM
            employees
    );

-- CTE (Common Table Expression): Find departments where the average salary is higher than the overall average salary
WITH
    DepartmentAverage AS (
        SELECT
            department_id,
            AVG(salary) AS average_salary
        FROM
            employees
        GROUP BY
            department_id
    )
SELECT
    department_id,
    (
        SELECT
            department_name
        FROM
            departments
        WHERE
            departments.department_id = DepartmentAverage.department_id
    ) AS department_name,
    average_salary
FROM
    DepartmentAverage
WHERE
    average_salary > (
        SELECT
            AVG(salary)
        FROM
            employees
    )
ORDER BY
    department_id ASC;