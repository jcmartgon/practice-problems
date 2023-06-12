-- Jesus Carlos Martinez Gonzalez
-- 11/06/2023
-- Revising Aggregation - The Count Function (https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem)
/*
 Query a count of the number of cities in CITY having a Population larger than 100,000. 
 */
SELECT COUNT(*)
FROM city
WHERE population > 100000;