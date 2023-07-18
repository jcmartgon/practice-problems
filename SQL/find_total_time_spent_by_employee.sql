-- Jesus Carlos Martinez Gonzalez
-- 17/07/2023
-- Find total time spent by each employee (https://leetcode.com/problems/find-total-time-spent-by-each-employee)
/*
 Table: Employees
 
 +-------------+------+
 | Column Name | Type |
 +-------------+------+
 | emp_id      | int  |
 | event_day   | date |
 | in_time     | int  |
 | out_time    | int  |
 +-------------+------+
 In SQL, (emp_id, event_day, in_time) is the primary key of this table.
 The table shows the employees' entries and exits in an office.
 event_day is the day at which this event happened, in_time is the minute at which the employee entered the office, and out_time is the minute at which they left the office.
 in_time and out_time are between 1 and 1440.
 It is guaranteed that no two events on the same day intersect in time, and in_time < out_time.
 */
SELECT event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS "total_time"
FROM employees
GROUP BY day,
    emp_id;