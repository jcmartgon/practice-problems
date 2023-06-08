-- Jesus Carlos Martinez Gonzalez
-- 07/06/2023
-- Japanese Cities Attributes (https://www.hackerrank.com/challenges/japanese-cities-attributes/problem)
/*
 Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
 */
SELECT *
FROM city
WHERE countrycode = "JPN";