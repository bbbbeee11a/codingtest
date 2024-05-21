# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person A LEFT JOIN Address B ON A.personId = B.personId;