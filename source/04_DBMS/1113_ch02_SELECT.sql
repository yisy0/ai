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

-- 3. 특정 행 출력 : WHERE절(조건절)에 비교연산자 : 같다(=), 다르다(!=, ^=, <>), >,..
SELECT EMPNO 사번, ENAME 이름, SAL 급여 FROM EMP WHERE SAL=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL!=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL^=3000;
SELECT EMPNO NO, ENAME NAME, SAL FROM EMP WHERE SAL<>3000;
    -- 비교연산자는 숫자, 문자, 날짜형 모두 가능
    -- ex1. 사원이름이 'A','B','C'로 시작하는 사원의 모든 열(필드)
    -- A < AA < AAA < AAAA <... < B < BA < ... < C 
    SELECT * FROM EMP WHERE ENAME < 'D';
    -- ex2. 81년도 이전에 입사한 사원의 모든 열(필드)
    SELECT * FROM EMP WHERE HIREDATE < '81/01/01';
    -- ex3. 부서번호(DEPTNO)가 10번인 사원의 모든 필드
    select * from emp where deptno=10;
    -- SQL문은 대소문자 구별없음. 데이터는 대소문자 구별
    -- ex4. 이름(ENAME)이 SCOTT인 직원의 모든 데이터(필드)
    SELect * from emp where ename = 'SCOTT';
    
-- 4.WHERE절(조건절)에 논리연산자 : AND  OR  NOT
    -- ex1. 급여(SAL)가 2000이상 3000이하인 직원의 모든 필드
    SELECT * FROM EMP WHERE SAL>=2000 AND SAL<=3000;
    -- ex2. 82년도 입사한 사원의 모든 필드
    SELECT * FROM EMP WHERE HIREDATE>='82/01/01' AND HIREDATE<='82/12/31';
    
    -- 날짜 표기법 셋팅 (현재:RR/MM/DD)
    ALTER SESSION SET NLS_DATE_FORMAT = 'RR/MM/DD';
    SELECT * FROM EMP 
        WHERE TO_CHAR(HIREDATE, 'MM-DD-YYYY') >='01-01-1982' 
            AND TO_CHAR(HIREDATE, '')<='12-31-1982';
    
    













