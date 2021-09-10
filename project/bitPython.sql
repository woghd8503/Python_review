--SYSTEM 계정으로 처리하는 부분 START
DROP USER bitPython CASCADE;

CREATE USER bitPython IDENTIFIED BY bitPython DEFAULT TABLESPACE users TEMPORARY TABLESPACE temp PROFILE DEFAULT;

GRANT CONNECT, RESOURCE TO bitPython;
GRANT CREATE VIEW, CREATE SYNONYM TO bitPython;

ALTER USER bitPython ACCOUNT UNLOCK;

conn bitPython/bitPython;
--SYSTEM 계정으로 처리하는 부분 END
--bitcamp START
--bitcamp로 접속했으므로 bitPython 사용자의 테이블이 생성
DROP TABLE student;

CREATE TABLE student(
    id NUMBER,                     -- 일련번호
    name VARCHAR(20) NOT NULL,
    age NUMBER,
    addr VARCHAR2(50),
    regdate DATE DEFAULT SYSDATE   -- 입력하지 않으면 현재시간
);

CREATE SEQUENCE student_id_swq;    -- id에 일련번호 입력할 시퀀스 객체 생성

INSERT INTO student (id, name, age, addr)
 VALUES(student_id_swq.nextval, '홍길동', 24, '지리산');
INSERT INTO student (id, name, age, addr)
 VALUES(student_id_swq.nextval, '임꺽정', 24, '구월산');
INSERT INTO student (id, name, age, addr)
 VALUES(student_id_swq.nextval, '장길산', 24, '해주');
INSERT INTO student (id, name, age, addr)
 VALUES(student_id_swq.nextval, '원빈', 24, '강원도');
INSERT INTO student (id, name, age, addr)
 VALUES(student_id_swq.nextval, '아이유', 24, '서울');

COMMIT;

ALTER TABLE student
 ADD CONSTRAINT student_id_pk PRIMARY KEY(id);

