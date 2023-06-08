-- Jesus Carlos Martinez Gonzalez
-- 07/06/2023
-- Revising the Select Query 1 (https://www.hackerrank.com/challenges/revising-the-select-query/problem)
/*
 Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.
 */
SELECT *
FROM city
WHERE countrycode = "USA"
    AND population > 100000;