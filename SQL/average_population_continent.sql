-- Jesus Carlos Martinez Gonzalez
-- 14/06/2023
-- Average Population from each continent (https://www.hackerrank.com/challenges/average-population-of-each-continent/problem)
/*
 Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer. 
 */
SELECT co.continent,
    FLOOR(AVG(ci.population))
FROM country co
    JOIN city ci ON co.code = ci.countrycode
GROUP BY co.continent;