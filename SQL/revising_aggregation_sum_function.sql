-- Jesus Carlos Martinez Gonzalez
-- 11/06/2023
-- Revising Aggregation - The Sum Function (https://www.hackerrank.com/challenges/revising-aggregations-the-sum-function/problem)
/*
 Query the total population of all cities in CITY where District is California.
 */
SELECT SUM(population)
FROM city
WHERE district = 'California';