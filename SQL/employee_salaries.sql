-- Jesus Carlos Martinez Gonzalez
-- 10/06/2023
-- Employee salary (https://www.hackerrank.com/challenges/salary-of-employees/problem)
/*
 Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  per month who have been employees for less than  months. 
 Sort your result by ascending employee_id.
 */
SELECT name
FROM employee
WHERE salary > 2000
    AND months < 10;