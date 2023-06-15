-- Jesus Carlos Martinez Gonzalez
-- 14/06/2023
-- Population Census (https://www.hackerrank.com/challenges/asian-population/problem)
/*
 Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'. 
 */
SELECT SUM(ci.population)
FROM city ci
    JOIN country co ON ci.countrycode = co.code
WHERE co.continent = 'Asia';