WITH TOP_3 AS (
    SELECT DISTINCT salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 3
)

SELECT coalesce(salary, NULL)
FROM TOP_3
ORDER BY salary ASC
limit 1