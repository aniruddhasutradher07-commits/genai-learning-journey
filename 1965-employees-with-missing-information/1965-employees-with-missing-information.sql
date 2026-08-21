SELECT employee_id
FROM (
    SELECT e.employee_id, e.name, s.salary
    FROM Employees e
    LEFT JOIN Salaries s ON e.employee_id = s.employee_id
    
    UNION
    
    SELECT s.employee_id, e.name, s.salary
    FROM Salaries s
    LEFT JOIN Employees e ON e.employee_id = s.employee_id
) AS combined
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id;
