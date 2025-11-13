-- [II] SELECT문 - 조회

-- 1. SELECT 문장 작성법
SELECT * FROM TAB; -- 현 계정이 가지고 있는 테이블 정보(실행:CTRL+ENTER)
SELECT * FROM DEPT;     -- DEPT 테이블의 모든 열, 모든 행
SELECT * FROM SALGRADE; -- SALGRADE 테이블이 모든 열, 모든 행
SELECT * FROM EMP;      -- EMP 테이블이 모든 열, 모든 행

-- 2. 특정 열만 출력
DESC EMP; 
    -- EMP테이블의 구조
SELECT EMPNO, ENAME, SAL, JOB FROM EMP; -- EMP테이블의 SELECT절에 지정된 열만 출력
SELECT EMPNO AS "사 번", ENAME AS "이 름", SAL AS "급여", JOB AS "직책"
    FROM EMP;  -- 열이름에 별칭을 두는 경우 EX. 열이름 AS "별칭"
SELECT EMPNO "사 번", ENAME "이 름", SAL "급여", JOB
    FROM EMP;  -- 열이름에 별칭을 두는 경우 EX. 열이름 "별칭", 열이름
SELECT EMPNO "사 번", ENAME 이름, SAL 급여, JOB
    FROM EMP;  -- 별칭에 SPACE가 없는 경우는 따옴표 생략가능

-- 3. 특정 행 출력 : WHERE절(조건절) -- 비교연산자 : 같다(=), 다르다(!=, ^=, <>), >,..
SELECT EMPNO 사번, ENAME 이름, SAL 급여 FROM EMP WHERE SAL=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL!=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL^=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL<>3000;













