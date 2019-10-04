-- 다음과 같은 스키마를 가지는 데이터베이스 테이블 friends 를 생성하시오
CREATE TABLE friends (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL,
    location TEXT NOT NULL
);

-- 해당 테이블에 다음과 같이 데이터를 입력하시오
INSERT INTO friends(name, location)
VALUES
('Justin', 'Seoul'),
('Simon', 'New York'),
('Chang', 'Las Vegas'),
('John', 'Sydney');

-- 스키마를 다음과 같이 변경하시오
ALTER TABLE friends ADD COLUMN married INTEGER;

-- 데이터를 다음과 같이 추가하시오
UPDATE friends SET married = 1 WHERE NAME = 'Justin';
UPDATE friends SET married = 0 WHERE NAME = 'Simon';
UPDATE friends SET married = 0 WHERE NAME = 'Chang';
UPDATE friends SET married = 1 WHERE NAME = 'John';