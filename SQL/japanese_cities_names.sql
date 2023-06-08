-- Jesus Carlos Martinez Gonzalez
-- 07/06/2023
-- Japanese Cities Names (https://www.hackerrank.com/challenges/japanese-cities-name/problem)
/*
 Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
 */
SELECT name
FROM city
WHERE countrycode = "JPN";