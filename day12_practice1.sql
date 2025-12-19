CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    salary INTEGER
);
INSERT INTO employees VALUES
(1, 'Amit', 25, 30000),
(2, 'Ravi', 30, 45000),
(3, 'Neha', 28, 40000),
(4, 'Sara', 35, 50000);

SELECT salary,COUNT(*)
FROM employees
WHERE salary > 35000;

SELECT age, MAX(salary)
FROM employees
GROUP BY age;

SELECT age, COUNT(*) FROM employees
GROUP BY age
HAVING COUNT(*) >1;