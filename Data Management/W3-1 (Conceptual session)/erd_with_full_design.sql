create database employeeDB;

use employeeDB;

create table
    department (department_id int, department_name varchar(50));

alter table department add constraint primary key (department_id);

create table
    employees (
        employee_id int primary key,
        name varchar(100),
        phone_number varchar(15),
        hire_date date default (current_date()),
        salary decimal(10, 2),
        department_id int,
        constraint fk_dept foreign key (department_id) references department (department_id)
    );

alter table employees
drop foreign key fk_dept;

alter table employees
add column email varchar(250);

insert into
    department (department_id, department_name)
values
    (1, 'Sales'),
    (2, 'Marketing'),
    (3, 'Human Resources'),
    (4, 'Finance'),
    (5, 'IT');

set
    SQL_SAFE_UPDATES = 0;

update department
set
    department_id = 7
where
    department_name = 'Finance';

set
    SQL_SAFE_UPDATES = 1;

alter table employees add foreign key (department_id) references department (department_id) on update cascade on delete cascade;

insert into
    employees
values
    (
        1,
        'John Doe',
        '+1-287-806-6832',
        '2018-03-06',
        119546.65,
        3,
        'johndoe@example.com'
    ),
    (
        2,
        'Jane Smith',
        '+1-816-810-6691',
        '2023-07-31',
        59908.52,
        5,
        'janesmith@example.com'
    ),
    (
        3,
        'Michael Johnson',
        '+1-385-273-9668',
        '2022-11-16',
        87056.31,
        1,
        'michaeljohnson@example.com'
    ),
    (
        4,
        'Emily Davis',
        '+1-847-474-2498',
        '2021-08-14',
        61295.82,
        2,
        'emilydavis@example.com'
    ),
    (
        5,
        'Chris Brown',
        '+1-709-582-2542',
        '2017-08-17',
        71652.57,
        1,
        'chrisbrown@example.com'
    ),
    (
        6,
        'Jessica Wilson',
        '+1-521-397-1653',
        '2019-05-22',
        89244.12,
        4,
        'jessicawilson@example.com'
    ),
    (
        7,
        'David Lee',
        '+1-204-567-1385',
        '2016-10-10',
        67985.33,
        5,
        'davidlee@example.com'
    ),
    (
        8,
        'Sarah Kim',
        '+1-631-841-2579',
        '2020-12-01',
        54923.75,
        3,
        'sarahkim@example.com'
    ),
    (
        9,
        'James Walker',
        '+1-951-396-7824',
        '2015-11-18',
        78613.90,
        2,
        'jameswalker@example.com'
    ),
    (
        10,
        'Laura Robinson',
        '+1-813-642-7839',
        '2022-01-29',
        73256.46,
        3,
        'laurarobinson@example.com'
    ),
    (
        11,
        'Daniel Harris',
        '+1-728-190-2643',
        '2018-09-23',
        102432.17,
        4,
        'danielharris@example.com'
    ),
    (
        12,
        'Sophia Martinez',
        '+1-925-317-1854',
        '2019-06-07',
        95432.50,
        1,
        'sophiamartinez@example.com'
    ),
    (
        13,
        'Matthew Clark',
        '+1-729-253-7610',
        '2023-03-21',
        50365.84,
        2,
        'matthewclark@example.com'
    ),
    (
        14,
        'Olivia Lewis',
        '+1-648-542-1659',
        '2017-04-15',
        83429.01,
        5,
        'olivialewis@example.com'
    ),
    (
        15,
        'Joshua Young',
        '+1-723-495-3172',
        '2016-08-02',
        64873.29,
        3,
        'joshuayoung@example.com'
    ),
    (
        16,
        'Ava Hall',
        '+1-702-813-4029',
        '2020-05-28',
        57564.92,
        2,
        'avahall@example.com'
    ),
    (
        17,
        'Andrew Allen',
        '+1-958-285-4172',
        '2021-11-05',
        78435.23,
        4,
        'andrewallen@example.com'
    ),
    (
        18,
        'Mia King',
        '+1-364-189-5203',
        '2018-02-14',
        89954.40,
        1,
        'miaking@example.com'
    ),
    (
        19,
        'Ryan Wright',
        '+1-208-740-6934',
        '2017-12-17',
        114283.19,
        5,
        'ryanwright@example.com'
    ),
    (
        20,
        'Chloe Scott',
        '+1-492-318-4671',
        '2023-10-09',
        60471.68,
        3,
        'chloescott@example.com'
    );

insert into
    employees
values
    (
        21,
        'Mr. X',
        '01795394787',
        '2023-10-09',
        '40000',
        5,
        'sharifaiub15@gmail.com'
    );

insert into
    employees (
        employee_id,
        name,
        phone_number,
        salary,
        department_id,
        email
    )
values
    (
        22,
        'Mr. Y',
        '01733726060',
        '20000',
        5,
        'sharifulislam18@ymail.com'
    );

update employees
set
    department_id = 4
where
    employee_id = 22;

delete from department
where
    department_id = 2;

select
    *
from
    department;

select
    *
from
    employees;