-- Jesus Carlos Martinez Gonzalez
-- 09/06/2023
-- Higher than 75 marks (https://www.hackerrank.com/challenges/more-than-75-marks/problem)
/*
 Query the Name of any student in STUDENTS who scored higher than  Marks. 
 Order your output by the last three characters of each name. 
 If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
 */
SELECT name
FROM students
WHERE marks > 75
ORDER BY SUBSTRING(name, -3, 3),
    id;