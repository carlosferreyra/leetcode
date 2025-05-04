# Write your MySQL query statement below
SELECT e.event_day as 'day', e.emp_id,  sum(e.out_time - e.in_time) AS total_time
FROM Employees e
GROUP BY e.event_day , e.emp_id ;