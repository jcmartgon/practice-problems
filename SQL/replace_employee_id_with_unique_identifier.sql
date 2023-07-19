-- Jesus Carlos Martinez Gonzalez
-- 18/07/2023
-- Replace employee id with unique identifier (https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier)
/*
 Table: Employees
 
 +---------------+---------+
 | Column Name   | Type    |
 +---------------+---------+
 | id            | int     |
 | name          | varchar |
 +---------------+---------+
 In SQL, id is the primary key for this table.
 Each row of this table contains the id and the name of an employee in a company.
 
 
 Table: EmployeeUNI
 
 +---------------+---------+
 | Column Name   | Type    |
 +---------------+---------+
 | id            | int     |
 | unique_id     | int     |
 +---------------+---------+
 In SQL, (id, unique_id) is the primary key for this table.
 Each row of this table contains the id and the corresponding unique id of an employee in the company.
 
 
 Show the unique ID of each user, If a user does not have a unique ID replace just show null.
 
 Return the result table in any order.
 
 The result format is in the following example.
 */
SELECT eu.unique_id,
    e.name
FROM employeeuni eu
    RIGHT JOIN employees e ON eu.id = e.id;