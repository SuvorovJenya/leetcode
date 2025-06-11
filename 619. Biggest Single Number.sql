-- Write your PostgreSQL query statement below
SELECT
    MAX(CASE WHEN num IS NOT NULL THEN num ELSE NULL END) as num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
)