-- [ III ] JOIN : 2개 이상의 테이블을 연결하여 데이터를 검색하는 방법 
SELECT * FROM EMP WHERE ENAME='SCOTT'; -- 사번,이름,업무,상사사번,입사일,급여,상여,부서번호
SELECT * FROM DEPT; -- 부서번호, 부서명, 부서위치
-- 사번~부서번호, 부서명, 부서위치
SELECT * FROM EMP, DEPT WHERE ENAME='SCOTT'; -- CROSS JOIN(무의미)

-- ▶ 1. EQUI JOIN : 공통필드값이 일치되는 조건만 JOIN ★★★
SELECT *                -- (3)
    FROM EMP E, DEPT D  -- (1) 이후 2,3번 줄에서 테이블의 별칭으로만 사용
    WHERE ENAME='SCOTT' AND E.DEPTNO=D.DEPTNO; -- (2)
SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, D.DEPTNO, DNAME, LOC
    FROM EMP E, DEPT D
    WHERE E.DEPTNO=D.DEPTNO;
SELECT EMPNO, ENAME, JOB, MGR, HIREDATE, SAL, COMM, D.*
    FROM EMP E, DEPT D
    WHERE E.DEPTNO=D.DEPTNO;
    -- ex. 급여가 2000이상인 직원의 이름, 직책, 급여, 부서명, 근무지
    SELECT ENAME, JOB, SAL, DNAME, LOC FROM EMP E, DEPT D; -- E 14개 x D 4개
    SELECT ENAME, JOB, SAL, DNAME, LOC FROM EMP E, DEPT D
        WHERE E.DEPTNO=D.DEPTNO AND SAL>=2000;
    -- ex. 20번 부서 직원만 이름, 부서번호, 근무지
    SELECT ENAME, DEPTNO, LOC
        FROM EMP E, DEPT D
        





