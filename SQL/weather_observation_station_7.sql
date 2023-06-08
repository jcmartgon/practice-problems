-- Jesus Carlos Martinez Gonzalez
-- 07/06/2023
-- Weather Observation Station 7 (https://www.hackerrank.com/challenges/weather-observation-station-7/problem)
/*
 Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
 */
SELECT DISTINCT city
FROM station
WHERE city REGEXP "[aeiou]$";