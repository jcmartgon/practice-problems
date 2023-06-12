-- Jesus Carlos Martinez Gonzalez
-- 11/06/2023
-- Average Population (https://www.hackerrank.com/challenges/average-population/problem)
/*
 Query the average population for all cities in CITY, rounded down to the nearest integer. 
 */
SELECT ROUND(AVG(population))
FROM city;