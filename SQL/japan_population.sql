-- Jesus Carlos Martinez Gonzalez
-- 11/06/2023
-- Japan Population (https://www.hackerrank.com/challenges/japan-population/problem)
/*
 Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN. 
 */
SELECT SUM(population)
FROM city
WHERE countrycode = 'JPN';