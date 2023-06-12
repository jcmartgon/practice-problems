-- Jesus Carlos Martinez Gonzalez
-- 11/06/2023
-- Weather Observation Station 13 (https://www.hackerrank.com/challenges/weather-observation-station-13/problem)
/*
 Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7880 and less than 137.2345 Truncate your answer to 4 decimal places.
 */
SELECT TRUNCATE(SUM(LAT_N), 4) AS 'LAT_N sum'
FROM station
WHERE LAT_N > 38.7880
    and LAT_N < 137.2345;