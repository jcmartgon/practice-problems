-- Jesus Carlos Martinez Gonzalez
-- 07/06/2023
-- Weather Observation Station 6 (https://www.hackerrank.com/challenges/weather-observation-station-6/problem)
/*
 Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
 */
SELECT DISTINCT city
FROM station
WHERE city REGEXP '^[aeiou]';