-- Jesus Carlos Martinez Gonzalez
-- 08/06/2023
-- Weather Observation Station 11 (https://www.hackerrank.com/challenges/weather-observation-station-11/problem)
/*
 Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
 */
SELECT DISTINCT city
FROM station
WHERE city REGEXP "^[^aeiouAEIOU]|[^aeiouAEIOU]$";