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
    SELECT ENAME, E.DEPTNO, LOC
        FROM EMP E, DEPT D
        WHERE E.DEPTNO = D.DEPTNO AND D.DEPTNO=20;
    -- ex. 근무지(LOC)가 CHICAGO인 사람의 이름, 급여, 부서번호를 출력
    SELECT ENAME, SAL, E.DEPTNO
        FROM EMP E, DEPT D
        WHERE E.DEPTNO=D.DEPTNO AND LOC='CHICAGO';
    -- ex. JOB이 'SALESMAN'이거나 'MANAGER'인 사원의 이름, 급여, 상여, 연봉, 부서명
            -- 연봉이 큰 순으로 정렬. 단, 연봉 = (SAL+COMM)*12
    SELECT ENAME, SAL, COMM, ( SAL + NVL(COMM,0) )*12 ANNUALSAL, DNAME
        FROM EMP E, DEPT D
        WHERE E.DEPTNO=D.DEPTNO AND JOB IN ('SALESMAN', 'MANAGER')
        ORDER BY ( SAL + NVL(COMM,0) )*12 DESC; -- ORDER BY ANNUALSAL DESC
    -- ex. COMM이 NULL이거나 0인 사원 중, 
        -- SAL이 1200이상인 사원의 이름, 급여, 부서번호, 부서명, 상여
        -- 부서명순, 급여 큰순 정렬
    SELECT ENAME, SAL, E.DEPTNO, DNAME, COMM FROM EMP E, DEPT D
        WHERE E.DEPTNO=D.DEPTNO AND (COMM IS NULL OR COMM=0)AND SAL>=1200
        ORDER BY DNAME, SAL DESC;
    -- 탄탄1. 뉴욕에서 근무하는 사원의 이름과 급여를 출력하시오
    SELECT ENAME, SAL FROM EMP E, DEPT D 
        WHERE E.DEPTNO=D.DEPTNO AND LOC='NEW YORK';
    -- 탄탄2. ACCOUNTING 부서 소속 사원의 이름과 입사일을 출력하시오
    SELECT ENAME, HIREDATE FROM EMP E, DEPT D
        WHERE E.DEPTNO=D.DEPTNO AND DNAME='ACCOUNTING';
    -- 탄탄3. 직급이 MANAGER인 사원의 이름, 부서명을 출력하시오
    SELECT ENAME, DNAME FROM EMP E, DEPT D
        WHERE E.DEPTNO=D.DEPTNO AND JOB='MANAGER';
    -- 탄탄4. Comm이 null이 아닌 사원의 이름, 급여, 부서코드, 근무지를 출력하시오.
    SELECT ENAME, SAL, E.DEPTNO, LOC FROM EMP E, DEPT D
        WHERE E.DEPTNO=D.DEPTNO AND COMM IS NOT NULL;

-- ▶ 2. Non-Equi Join : 동일한 컬럼없이 다른 조건을 사용하여 조인
SELECT * FROM EMP WHERE ENAME='SCOTT';
SELECT * FROM SALGRADE;
SELECT * FROM EMP, SALGRADE WHERE ENAME='SCOTT' AND SAL>=LOSAL AND SAL<=HISAL;
SELECT * FROM EMP, SALGRADE WHERE ENAME='SCOTT' AND SAL BETWEEN LOSAL AND HISAL;
    -- ex. 모든사원의 사번, 이름, 급여, 급여등급(1등급, 2등급..), 상사사번
    SELECT EMPNO, ENAME, SAL, GRADE||'등급' "GRADE", MGR
        FROM EMP, SALGRADE
        WHERE SAL BETWEEN LOSAL AND HISAL;

    -- 탄탄1. Comm이 null이 아닌 사원의 이름, 급여, 등급, 부서번호, 부서이름, 근무지를 출력하시오.

-	이름, 급여, 입사일, 급여등급

-	이름, 급여, 급여등급, 연봉, 부서명을 부서명순으로 정렬하여 출력. 부서가 같으면 연봉순. 연봉=(sal+comm)*12 comm이 null이면 0

-	이름, 업무, 급여, 등급, 부서코드, 부서명 출력. 급여가 1000~3000사이. 정렬조건 : 부서별, 부서같으면 업무별, 업무같으면 급여 큰순

-	이름, 급여, 등급, 입사일, 근무지. 81년에 입사한 사람. 등급 큰순






