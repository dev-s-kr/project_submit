-- 기본 위치를 database_3으로 설정
USE database_3;

-- employees라는 테이블을 생성
CREATE TABLE employees (
	-- id라는 컬럼을 생성. 데이터 타입은 Int, 기본 키이며 값이 자동으로 1씩 증가
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- name이라는 컬럼을 생성. 데이터 타입은 Varchar, 최대 길이는 100
    name VARCHAR(100),
    -- position이라는 컬럼을 생성. 데이터 타입은 Varchar, 최대 길이는 100
    position VARCHAR(100),
    -- salary라는 컬럼을 생성. 데이터 타입은 Decimal, 소수점 2자리 포함 총 10자리 수 표현
    salary DECIMAL(10, 2)
);

-- employees 테이블의 name, position, salary 컬럼에 다음 값을 추가
INSERT INTO employees (name, position, salary) VALUES
    ("혜린", "PM", 90000),
	("은우", "Frontend", 80000),
	("가을", "Backend", 92000),
	("지수", "Frontend", 78000),
	("민혁", "Frontend", 96000),
	("하온", "Backend", 130000);