-- Jesus Carlos Martinez Gonzalez
-- 07/06/2023
-- Weather Observation Station 4 (https://www.hackerrank.com/challenges/weather-observation-station-4/problem)
/*
 Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
 */
SELECT COUNT(city) - COUNT(DISTINCT city)
FROM station;