# Write your MySQL query statement below
SELECT DISTINCT email 
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
