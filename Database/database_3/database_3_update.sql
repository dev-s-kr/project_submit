-- employees에서 position이 "PM"인 데이터의 salary를 salary * 1.1한 값으로 업데이트
UPDATE employees SET salary = salary * 1.1 WHERE position = "PM";

-- employees에서 position이 "Backend"인 데이터의 salary를 salary * 1.05한 값으로 업데이트
UPDATE employees SET salary = salary * 1.05 WHERE position = "Backend";