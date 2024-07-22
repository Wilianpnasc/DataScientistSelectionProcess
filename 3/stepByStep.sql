-- Selecionar o departamento inicial de cada funcionário
WITH FirstDepartment AS (
    SELECT
        edh.employee_id,
        edh.department_id,
        ROW_NUMBER() OVER (PARTITION BY edh.employee_id ORDER BY edh.start_date) AS rn
    FROM
        employee_department_history edh
),

-- Posteriormente, selecionar o departamento atual de cada funcionário
CurrentDepartment AS (
    SELECT
        edh.employee_id,
        edh.department_id
    FROM
        employee_department_history edh
    WHERE
        edh.end_date IS NULL
),

-- Contar o número de departamentos distintos de cada funcionário
DepartmentCount AS (
    SELECT
        edh.employee_id,
        COUNT(DISTINCT edh.department_id) AS department_count
    FROM
        employee_department_history edh
    GROUP BY
        edh.employee_id
)

-- Selecionar informações para o relatório final
SELECT
    e.employee_id,
    e.employee_name,
    d_first.department_name AS first_department_name,
    d_current.department_name AS current_department_name,
    dc.department_count
FROM
    employees e
JOIN FirstDepartment fd ON e.employee_id = fd.employee_id AND fd.rn = 1
JOIN departments d_first ON fd.department_id = d_first.department_id
JOIN CurrentDepartment cd ON e.employee_id = cd.employee_id
JOIN departments d_current ON cd.department_id = d_current.department_id
JOIN DepartmentCount dc ON e.employee_id = dc.employee_id;

