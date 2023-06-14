-- Jesus Carlos Martinez Gonzalez
-- 13/06/2023
-- Weather Observation 16 (https://www.hackerrank.com/challenges/weather-observation-station-16/problem)
/*
 Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to 4 decimal places. 
 */
SELECT ROUND(lat_n, 4)
FROM station
WHERE lat_n > 38.7780
ORDER BY lat_n
LIMIT 1;