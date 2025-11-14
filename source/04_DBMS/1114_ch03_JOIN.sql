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

    -- 탄탄1. Comm이 null이 아닌 사원의 이름, 급여, 등급, 부서번호, 부서이름, 근무지를 출력.
    SELECT ENAME, SAL, GRADE, E.DEPTNO, DNAME, LOC
        FROM EMP E, DEPT D, SALGRADE
        WHERE E.DEPTNO=D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL
            AND COMM IS NOT NULL;
    -- 탄탄2. 이름, 급여, 입사일, 급여등급
    SELECT ENAME, SAL, HIREDATE, GRADE
        FROM EMP, SALGRADE
        WHERE SAL BETWEEN LOSAL AND HISAL;
    -- 탄탄3. 이름, 급여, 급여등급, 연봉, 부서명을 부서명순으로 정렬하여 출력.
        -- 부서가 같으면 연봉순. 연봉=(sal+comm)*12 comm이 null이면 0
    SELECT ENAME, SAL, GRADE, (SAL+NVL(COMM,0))*12 연봉, DNAME
        FROM EMP E, DEPT D, SALGRADE
        WHERE E.DEPTNO=D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL
        ORDER BY DNAME, 연봉;
    -- 탄탄4. 이름, 업무, 급여, 등급, 부서코드, 부서명 출력. 급여가 1000~3000사이. 
        -- 정렬조건 : 부서별, 부서같으면 업무별, 업무같으면 급여 큰순
    SELECT ENAME, JOB, SAL, GRADE, E.DEPTNO, DNAME
        FROM EMP E, DEPT D, SALGRADE
        WHERE E.DEPTNO=D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL 
            AND SAL BETWEEN 1000 AND 3000
        ORDER BY DEPTNO, JOB, SAL DESC;
    -- 탄탄5. 이름, 급여, 등급, 입사일, 근무지. 81년에 입사한 사람. 등급 큰순
    SELECT ENAME, SAL, GRADE, HIREDATE, LOC
        FROM EMP E, DEPT D, SALGRADE
        WHERE E.DEPTNO=D.DEPTNO AND SAL BETWEEN LOSAL AND HISAL
            AND TO_CHAR(HIREDATE, 'RR') = 81
        ORDER BY GRADE;

-- ★ <총 연습문제> Part1
--1. 모든 사원에 대한 이름, 부서번호, 부서명을 출력하는 SELECT 문장을 작성하여라.
SELECT ENAME, E.DEPTNO, DNAME 
  FROM EMP E, DEPT D 
  WHERE E.DEPTNO=D.DEPTNO;

--2. NEW YORK에서 근무하고 있는 사원에 대하여 이름, 업무, 급여, 부서명을 출력
SELECT ENAME, JOB, SAL, DNAME 
  FROM EMP E, DEPT D 
  WHERE E.DEPTNO=D.DEPTNO AND LOC='NEW YORK';
  
--3. 보너스를 받는 사원에 대하여 이름,부서명,위치를 출력
SELECT ENAME, COMM, DNAME, LOC 
  FROM EMP E, DEPT D
  WHERE E.DEPTNO=D.DEPTNO AND COMM>0;

--4. 이름 중 L자가 있는 사원에 대하여 이름,업무,부서명,위치를 출력
SELECT ENAME, JOB, DNAME, LOC 
  FROM EMP E, DEPT D
  WHERE E.DEPTNO=D.DEPTNO AND ENAME LIKE '%L%';
    
--5. 사번, 사원명, 부서코드, 부서명을 검색하라(단, 사원명기준으로 오름차순 정렬)
SELECT EMPNO, ENAME, D.DEPTNO, DNAME
  FROM EMP E, DEPT D
  WHERE E.DEPTNO=D.DEPTNO
  ORDER BY ENAME;
  
--6. 사번, 사원명, 급여, 부서명을 검색하라. 
    --단 급여가 2000이상인 사원에 대하여 급여를 기준으로 내림차순으로 정렬하시오
SELECT EMPNO, ENAME, SAL, DNAME
  FROM EMP E, DEPT D
  WHERE E.DEPTNO=D.DEPTNO AND SAL>=2000
  ORDER BY SAL DESC;
  
--7. 사번, 사원명, 업무, 급여, 부서명을 검색하시오. 단 업무가 MANAGER이며 급여가 2500이상인
-- 사원에 대하여 사번을 기준으로 오름차순으로 정렬하시오.
SELECT EMPNO, ENAME, JOB, SAL, DNAME
  FROM EMP E, DEPT D
  WHERE E.DEPTNO=D.DEPTNO AND JOB='MANAGER' AND SAL>=2500
  ORDER BY EMPNO;
    
--8. 사번, 사원명, 업무, 급여, 등급을 검색하시오(단, 급여기준 내림차순으로 정렬)
SELECT EMPNO, ENAME, JOB, SAL, GRADE
  FROM EMP, SALGRADE
  WHERE SAL BETWEEN LOSAL AND HISAL
  ORDER BY SAL DESC;

-- ▶ 3. SELF-JOIN 
SELECT EMPNO, ENAME, MGR FROM EMP WHERE ENAME='SMITH'; -- 7902?
SELECT EMPNO, ENAME FROM EMP;
SELECT WORKER.EMPNO, WORKER.ENAME, WORKER.MGR, MANAGER.EMPNO, MANAGER.ENAME 메니저
  FROM EMP WORKER, EMP MANAGER
  WHERE WORKER.ENAME = 'SMITH' AND WORKER.MGR=MANAGER.EMPNO;
  -- ex. 사번, 이름, 상사사번, 상사이름
  SELECT W.EMPNO, W.ENAME, W.MGR, M.EMPNO, M.ENAME
    FROM EMP W, EMP M
    WHERE W.MGR = M.EMPNO;
  -- ex. 'SMITH의 상사는 FORD다' 포맷으로 출력
  SELECT W.ENAME || '의 상사는 ' || M.ENAME || '다'  MESSAGE
    FROM EMP W, EMP M
    WHERE W.MGR=M.EMPNO;
  -- 탄탄ex. 매니저가 KING인 사원들의 이름과 직급을 출력하시오
  SELECT W.ENAME, W.JOB
    FROM EMP W, EMP M
    WHERE W.MGR = M.EMPNO AND M.ENAME='KING';
  SELECT EMPNO FROM EMP WHERE ENAME='KING'; -- KING의 사번:7839
  SELECT ENAME, JOB FROM EMP WHERE MGR=7839; -- 상사의 사번이 7839인 사람

-- ▶ 4. OUTER JOIN : EQUI/SELF JOIN시 조건에 만족하니 않는 행까지 나타나게
-- (1) SELF JOIN에서의 OUTER JOIN
SELECT W.ENAME, W.MGR, M.EMPNO, M.ENAME
  FROM EMP W, EMP M
  WHERE W.MGR = M.EMPNO(+);
  -- ex. 'SMITH의 상사는 FORD다' - 'KING의 상사는 없다'
  SELECT W.ENAME || '의 상사는 ' || NVL(M.ENAME, '없') || '다'
    FROM EMP W, EMP M
    WHERE W.MGR = M.EMPNO(+);
  -- ex. 말단사원
  SELECT M.ENAME
    FROM EMP W, EMP M
    WHERE W.MGR(+) = M.EMPNO AND W.ENAME IS NULL;

-- (2) EQUI JOIN에서의 OUTER JOIN
SELECT * FROM EMP; -- 14행 (10,20,30)
SELECT * FROM DEPT; -- 4행 (10,20,30,40)
SELECT * FROM EMP E,  DEPT D 
  WHERE E.DEPTNO(+)=D.DEPTNO; -- 40번 부서 포함

-- Part2
--1. 이름, 직속상사명
SELECT W.ENAME, M.ENAME MANAGER
  FROM EMP W, EMP M
  WHERE W.MGR = M.EMPNO;
  
--2. 이름, 급여, 업무, 직속상사명
SELECT W.ENAME, W.SAL, W.JOB, M.ENAME MANAGER
  FROM EMP W, EMP M
  WHERE W.MGR = M.EMPNO;
  
--3. 이름, 급여, 업무, 직속상사명 . (상사가 없는 직원까지 전체 직원 다 출력. 상사가 없을 시 '없음'으로 출력)
SELECT W.ENAME, W.SAL, W.JOB, NVL(M.ENAME,'없음') MANAGER
  FROM EMP W, EMP M
  WHERE W.MGR = M.EMPNO(+);
  
--4. 이름, 급여, 부서명, 직속상사명
SELECT W.ENAME, W.SAL, DNAME, M.ENAME
  FROM EMP W, EMP M, DEPT D
  WHERE W.MGR = M.EMPNO AND W.DEPTNO=D.DEPTNO;
  
--5. 상사가 없는 직원과 상사가 있는 직원 모두에 대해 이름, 급여, 부서코드, 부서명, 근무지,
  --직속상사명을 출력하시오(단, 직속상사가 없을 경우 직속상사명에는 ‘없음’으로)
SELECT W.ENAME, W.SAL, W.DEPTNO, DNAME, LOC, NVL(M.ENAME, '없음') MANAGER
  FROM EMP W, EMP M, DEPT D
  WHERE W.MGR = M.EMPNO(+) AND W.DEPTNO=D.DEPTNO;
  
--6. 이름, 급여, 등급, 부서명, 직속상사명. 급여가 2000이상인 사람
SELECT W.ENAME, W.SAL, GRADE, DNAME, M.ENAME MANAGER
  FROM EMP W, EMP M, DEPT D, SALGRADE
  WHERE W.MGR = M.EMPNO AND W.DEPTNO=D.DEPTNO 
    AND W.SAL BETWEEN LOSAL AND HISAL
    AND W.SAL>=2000;
  
--7. 이름, 급여, 등급, 부서명, 직속상사명, (직속상사가 없는 직원까지 부서명 순 정렬)
SELECT W.ENAME, W.SAL, GRADE, DNAME, M.ENAME MANAGER
  FROM EMP W, EMP M, DEPT D, SALGRADE
  WHERE W.MGR = M.EMPNO(+) AND W.DEPTNO=D.DEPTNO 
    AND W.SAL BETWEEN LOSAL AND HISAL
  ORDER BY DNAME;
    
--8. 이름, 급여, 등급, 부서명, 연봉, 직속상사명. 연봉=(SAL+COMM)*12으로 계산
SELECT W.ENAME, W.SAL, GRADE, DNAME, (W.SAL+NVL(W.COMM,0))*12 연봉, M.ENAME MANAGER
  FROM EMP W, EMP M, DEPT D, SALGRADE
  WHERE W.MGR = M.EMPNO AND W.DEPTNO=D.DEPTNO 
    AND W.SAL BETWEEN LOSAL AND HISAL;
  
--9. 8번을 부서명 순 부서가 같으면 급여가 큰 순 정렬
SELECT W.ENAME, W.SAL, GRADE, DNAME, (W.SAL+NVL(W.COMM,0))*12 연봉, M.ENAME MANAGER
  FROM EMP W, EMP M, DEPT D, SALGRADE
  WHERE W.MGR = M.EMPNO AND W.DEPTNO=D.DEPTNO 
    AND W.SAL BETWEEN LOSAL AND HISAL
  ORDER BY DNAME, SAL DESC;
  
--10. 사원명, 상사명, 상사의 상사명을 검색하시오(self join)
SELECT W.ENAME, M.ENAME MANAGER, MM.ENAME TOPMANAGER
  FROM EMP W, EMP M, EMP MM
  WHERE W.MGR=M.EMPNO AND M.MGR=MM.EMPNO;

--11. 위의 결과에서 상위 상사가 없는 모든 직원의 이름도 출력되도록 수정하시오(outer join)
SELECT W.ENAME, M.ENAME MANAGER, MM.ENAME TOPMANAGER
  FROM EMP W, EMP M, EMP MM
  WHERE W.MGR=M.EMPNO(+) AND M.MGR=MM.EMPNO(+)