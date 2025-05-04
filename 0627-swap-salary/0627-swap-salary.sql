# Write your MySQL query statement below
UPDATE Salary s
SET s.sex = IF(s.sex = 'f', 'm','f')
