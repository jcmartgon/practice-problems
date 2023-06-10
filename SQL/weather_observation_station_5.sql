-- Jesus Carlos Martinez Gonzalez
-- 09/06/2023
-- Weather Observation Station 5 (https://www.hackerrank.com/challenges/weather-observation-station-5/problem)
/*
 Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). 
 If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
 */
SELECT city,
    length(city) as len
FROM station
ORDER BY len DESC,
    city
LIMIT 1;
SELECT city,
    length(city) as len
FROM station
ORDER BY len,
    city
LIMIT 1;