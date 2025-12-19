CREATE TABLE employees (
  id INTEGER PRIMARY KEY,
  name TEXT,
  age INTEGER,
  salary INTEGER
);

INSERT INTO employees VALUES
(1, 'Amit', 25, 30000),
(2, 'Ravi', 30, 40000),
(3, 'Neha', 28, 35000);

SELECT * FROM employees
WHERE age > 26;
