-- employees의 모든 데이터를 조회
SELECT * FROM employees;

-- employees에서 position이 "Frontend"이며 salary가 90000 이하인 값의 name과 salary를 조회
SELECT name, salary FROM employees WHERE position = "Frontend" AND salary <= 90000;

-- position으로 그룹화된 employees에서 position과, salary의 평균값을 position_salary_avg라는 칼럼으로 조회
SELECT position, avg(salary) AS position_salary_avg FROM employees GROUP BY position;