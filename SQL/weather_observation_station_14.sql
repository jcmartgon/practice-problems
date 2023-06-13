-- Jesus Carlos Martinez Gonzalez
-- 12/06/2023
-- Weather Observation 14 (https://www.hackerrank.com/challenges/weather-observation-station-14/problem)
/*
 Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345. Truncate your answer to 4 decimal places.
 */
SELECT TRUNCATE(lat_n, 4)
FROM station
WHERE lat_n < 137.2345
ORDER BY lat_n DESC
LIMIT 1;