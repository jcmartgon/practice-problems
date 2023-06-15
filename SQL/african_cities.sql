-- Jesus Carlos Martinez Gonzalez
-- 14/06/2023
-- African Cities (https://www.hackerrank.com/challenges/african-cities/problem)
/*
 Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
 */
SELECT ci.name
FROM city ci
    JOIN country co ON ci.countrycode = co.code
WHERE co.continent = 'Africa';