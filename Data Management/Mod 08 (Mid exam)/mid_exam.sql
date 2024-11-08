use DUMMYDB;

-- 02. Show employee first name and manager id
select
    MAN.FIRST_NAME as EMPLOYEE,
    EMP.MANAGER_ID as MANAGER_ID
from
    EMPLOYEES as EMP
    join EMPLOYEES as MAN on EMP.EMPLOYEE_ID = MAN.MANAGER_ID;

/* 03. 
Create a table of Employees which has the following fields:
Employee_Id
First Name
Last Name
Date of Birth
Department Id
Salary

Create a table Projects with the following fields:	
Project ID
Project Name
Start Date
End Date
Budget

Create a table Employee_Projects with the following fields:
Employee ID	
Project ID

Ensure that each employee can work on multiple projects and a project can have multiple employees.
 */
CREATE DATABASE mid_exam;

USE mid_exam;

CREATE TABLE
    Employees (
        Employee_Id INT PRIMARY KEY,
        First_Name VARCHAR(50) NOT NULL,
        Last_Name VARCHAR(50) NOT NULL,
        Date_Of_Birth DATE NOT NULL,
        Department_Id INT,
        Salary FLOAT
    );

CREATE TABLE
    Projects (
        Project_Id INT PRIMARY KEY,
        Project_Name VARCHAR(100) NOT NULL,
        Start_Date DATE NOT NULL,
        End_Date DATE,
        Budget DOUBLE
    );

CREATE TABLE
    Employee_Projects (
        Employee_Id INT,
        Project_Id INT,
        CONSTRAINT composit_pk PRIMARY KEY (Employee_Id, Project_Id),
        CONSTRAINT employee_is_fk FOREIGN KEY (Employee_Id) REFERENCES Employees (Employee_Id),
        CONSTRAINT project_is_fk FOREIGN KEY (Project_Id) REFERENCES Projects (Project_Id)
    );

-- 04. Using the dummydb, write an SQL query to get the third-highest salary in the employees table.
SELECT DISTINCT
    salary
FROM
    employees
ORDER BY
    salary DESC
LIMIT
    1
OFFSET
    2;

-- 05. Write a query to show the department names and the number of employees in each department.
SELECT
    dept.department_name AS departments,
    COUNT(emp.employee_id) AS employees
FROM
    departments AS dept
    LEFT JOIN employees AS emp ON dept.department_id = emp.department_id
GROUP BY
    dept.department_name;

-- 06. Illustrate INNER JOIN, LEFT JOIN, RIGHT JOIN, and CROSS JOIN with examples using the employees and departments tables.
select
    *
from
    EMPLOYEES
    inner join DEPARTMENTS using (DEPARTMENT_ID);

select
    *
from
    EMPLOYEES
    left join DEPARTMENTS using (DEPARTMENT_ID);

select
    *
from
    EMPLOYEES
    right join DEPARTMENTS using (DEPARTMENT_ID);

select
    *
from
    EMPLOYEES
    cross join DEPARTMENTS using (DEPARTMENT_ID);

-- 07. Write an example query using CTE to show the names of employees whose salary is higher than the average salary.
WITH
    average_salary AS (
        SELECT
            AVG(salary) AS AvgSalary
        FROM
            employees
    )
SELECT
    first_name,
    last_name,
    salary
FROM
    employees,
    average_salary
WHERE
    salary > average_salary.AvgSalary;

-- 08. Write a query to display the names of employees who earn a salary less than the employee "Steven King".
SELECT
    first_name,
    last_name
FROM
    employees
WHERE
    salary < (
        SELECT
            salary
        FROM
            employees
        WHERE
            first_name = 'Steven'
            AND last_name = 'King'
    );

-- 09. Write a query to find the department names and the names of the managers for each department.
SELECT
    department_name,
    CONCAT (employees.first_name, ' ', employees.last_name) AS manager_name
FROM
    departments
    JOIN employees ON departments.manager_id = employees.employee_id;

-- 10. Write a query to display the names of all cities where departments are located.
SELECT
    locations.city AS cities,
    departments.department_name AS department
FROM
    departments
    JOIN locations ON departments.location_id = locations.location_id;

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --