-- Jesus Carlos Martinez Gonzalez
-- 10/06/2023
-- Type of Triangle (https://www.hackerrank.com/challenges/what-type-of-triangle/problem)
/*
 Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:
 
 Equilateral: It's a triangle with  sides of equal length.
 Isosceles: It's a triangle with  sides of equal length.
 Scalene: It's a triangle with  sides of differing lengths.
 Not A Triangle: The given values of A, B, and C don't form a triangle.
 */
SELECT CASE
        WHEN a + b <= c
        OR b + c <= a
        OR a + c <= b THEN 'Not A Triangle'
        WHEN a = b
        AND a = c THEN 'Equilateral'
        WHEN a = b
        OR a = c
        OR b = c THEN 'Isosceles'
        ELSE 'Scalene'
    END as 'type'
FROM TRIANGLES