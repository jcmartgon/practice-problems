-- Jesus Carlos Martinez Gonzalez
-- 08/06/2023
-- Weather Observation Station 8 (https://www.hackerrank.com/challenges/weather-observation-station-8/problem)
/*
 Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
 */
SELECT DISTINCT city
FROM station
WHERE city REGEXP "^[aeiou].*[aeiou]$";