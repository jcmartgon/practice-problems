-- Jesus Carlos Martinez Gonzalez
-- 187/07/2023
-- Number of unique subjects taught by each teacher (https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher)
/*
 Table: Teacher
 
 +-------------+------+
 | Column Name | Type |
 +-------------+------+
 | teacher_id  | int  |
 | subject_id  | int  |
 | dept_id     | int  |
 +-------------+------+
 In SQL, (subject_id, dept_id) is the primary key for this table.
 Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
 
 
 Calculate the number of unique subjects each teacher teaches in the university.
 
 Return the result table in any order.
 
 The result format is shown in the following example.
 */
SELECT teacher_id,
    COUNT(DISTINCT subject_id) as cnt
FROM teacher
GROUP BY teacher_id;