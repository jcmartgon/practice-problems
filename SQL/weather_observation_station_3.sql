-- Jesus Carlos Martinez Gonzalez
-- 07/06/2023
-- Weather Observation Station 3 (https://www.hackerrank.com/challenges/weather-observation-station-3/problem)
/*
 Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
 */
SELECT DISTINCT city
FROM station
WHERE id % 2 = 0;