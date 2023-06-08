-- Jesus Carlos Martinez Gonzalez
-- 07/06/2023
-- Revising the Select Query 2 (https://www.hackerrank.com/challenges/revising-the-select-query-2/problem)
/*
 Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
 */
SELECT name
FROM city
WHERE countrycode = "USA"
    AND population > 120000;