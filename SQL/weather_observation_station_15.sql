-- Jesus Carlos Martinez Gonzalez
-- 13/06/2023
-- Weather Observation 15 (https://www.hackerrank.com/challenges/weather-observation-station-15/problem)
/*
 Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345. Round your answer to  decimal places.
 */
SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n < 137.2345
ORDER BY lat_n DESC
LIMIT 1;