-- Jesus Carlos Martinez Gonzalez
-- 08/06/2023
-- Weather Observation Station 12 (https://www.hackerrank.com/challenges/weather-observation-station-12/problem)
/*
 Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
 */
SELECT DISTINCT city
FROM station
WHERE city REGEXP "^[^aeiouAEIOU].*[^aeiouAEIOU]$";