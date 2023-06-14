-- Jesus Carlos Martinez Gonzalez
-- 13/06/2023
-- Weather Observation 17 (https://www.hackerrank.com/challenges/weather-observation-station-17/problem)
/*
 Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780. Round your answer to 4 decimal places. 
 */
SELECT ROUND(long_w, 4)
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
LIMIT 1;