-- Jesus Carlos Martinez Gonzalez
-- 11/06/2023
-- Weather Observation Station 2 (https://www.hackerrank.com/challenges/weather-observation-station-2/problem)
/*
 Query the following two values from the STATION table:
 
 The sum of all values in LAT_N rounded to a scale of 2 decimal places.
 The sum of all values in LONG_W rounded to a scale of 2 decimal places.
 */
SELECT ROUND(SUM(LAT_N), 2),
    ROUND(SUM(LONG_W), 2)
FROM station;