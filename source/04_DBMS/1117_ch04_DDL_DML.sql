-- [ IV ] DDL, DCL, DML
/* SQL
(1) DCL : 
  사용자계정생성 CREATE USER, 권한부여 GRANT
  권한박탈      REVOKE,      사용자계정삭제 DROP USER
  트렌젝션 명령어(ROLLBACK, COMMIT)
(2) DDL :
  테이블생성 CREATE TABLE, 테이블구조변경 ALTER TABLE, 테이블삭제 DROP TABLE
(3) DML : CRUD
  입력 INSERT, 검색 SELECT, 수정 UPDATE, 삭제 DELETE - DML은 취소 가능 */

----------------
--- ★ DDL ★ ---
----------------
-- 1. 테이블 생성(CREATE TABLE 테이블명...) : 테이블의 구조를 정의
  -- ORACLE 타입 : NUMBER(38이하의 자릿수), DATE, VARCHAR2(4000이하의 바이트수), CLOB
CREATE TABLE BOOK(
  BOOKID NUMBER(4),      -- BOOKID필드의 타입은 숫자4자리
  BOOKNAME VARCHAR2(20), -- BOOKNAME필드의 타입은 문자 20바이트(한글1자=3바이트)
  PUBLISHER VARCHAR2(20),
  RDATE     DATE,        -- RDATE필드의 타입은 DATE형(날짜+시간)
  PRICE     NUMBER(8,2), -- PRICE필드의 타입은 숫자 전체8자리 중 소숫점 2자리
  PRIMARY KEY(BOOKID)    -- 제약조건 : BOOKID를 주키(PRIMARY KEY) 필드로
);
SELECT * FROM BOOK;
DESC BOOK;
DROP TABLE BOOK; -- 2. 테이블 삭제(DROP TABLE 테이블명)
CREATE TABLE BOOK(
  BOOKID NUMBER(4) PRIMARY KEY,      -- BOOKID필드의 타입은 숫자4자리
  BOOKNAME VARCHAR2(20), -- BOOKNAME필드의 타입은 문자 20바이트(한글1자=3바이트)
  PUBLISHER VARCHAR2(20),
  RDATE     DATE,        -- RDATE필드의 타입은 DATE형(날짜+시간)
  PRICE     NUMBER(8,2)  -- PRICE필드의 타입은 숫자 전체8자리 중 소숫점 2자리
);
SELECT * FROM EMP;
SELECT * FROM DEPT; -- 10,20,30,40부서
INSERT INTO EMP VALUES (7369, '홍길동', NULL, NULL, NULL, NULL, NULL, 40);
-- DEPT와 유사한 DEPT01 : DEPTNO(숫2-PK), DNAME(문14), LOC(문13)
CREATE TABLE DEPT01(
  DEPTNO NUMBER(2) PRIMARY KEY,
  DNAME  VARCHAR2(14),
  LOC    VARCHAR2(13)
);
INSERT INTO DEPT01 VALUES (10, '전산실', '신림');
SELECT * FROM DEPT01;
ROLLBACK; -- DML 취소
-- EMP와 유사한 EMP01:EMPNO(숫4-PK), ENAME(문10), HIREDATE(날), SAL(숫7.2), DEPTNO(수2-FK)
CREATE TABLE EMP01(
  EMPNO    NUMBER(4) PRIMARY KEY,
  ENAME    VARCHAR2(10),
  HIREDATE DATE,
  SAL      NUMBER(7, 2), -- 소숫점앞 5자리 소수점뒤 2자리. 총 7자리
  DEPTNO   NUMBER(2) REFERENCES DEPT01(DEPTNO) -- 외래키(FOREIGN KEY) 제약조건
);
DROP TABLE EMP01;
CREATE TABLE EMP01(
  EMPNO    NUMBER(4),
  ENAME    VARCHAR2(10),
  HIREDATE DATE,
  SAL      NUMBER(7, 2), -- 소숫점앞 5자리 소수점뒤 2자리. 총 7자리
  DEPTNO   NUMBER(2), -- 외래키(FOREIGN KEY) 제약조건
  PRIMARY KEY(EMPNO),
  FOREIGN KEY(DEPTNO) REFERENCES DEPT01(DEPTNO)
);
INSERT INTO EMP01 VALUES (1001, '홍길동', SYSDATE, 9999, 10);
COMMIT; -- 트랜젝션 영역에 쌓여 있는 DML명령어들을 ORACLE에 일괄 적용

----------------
--- ★ DML ★ ---
----------------
-- 1. INSERT INTO 테이블명 (필드명1, 필드명2, ...) VALUES (값1, 값2, ..);
   -- INSERT INTO 테이블명 VALUES (값1, 값2,..값N);
SELECT * FROM DEPT01;














