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

SELECT COUNT(*) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary),MAX(salary)
FROM employees;
SELECT age, AVG(salary)
FROM employees
GROUP BY age;
SELECT age,COUNT(*) FROM employees
GROUP BY age;
SELECT age, AVG(salary) 
FROM employees
GROUP BY age
HAVING AVG(salary)>40000;

SELECT age, AVG(salary) AS avg_salary
FROM employees
GROUP BY age
ORDER BY avg_salary DESC;

