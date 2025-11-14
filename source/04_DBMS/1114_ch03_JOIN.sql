-- [ III ] JOIN : 2개 이상의 테이블을 연결하여 데이터를 검색하는 방법 
SELECT * FROM EMP WHERE ENAME='SCOTT'; -- 사번,이름,업무,상사사번,입사일,급여,상여,부서번호
SELECT * FROM DEPT; -- 부서번호, 부서명, 부서위치
-- 사번~부서번호, 부서명, 부서위치
SELECT * FROM EMP, DEPT WHERE ENAME='SCOTT'; -- CROSS JOIN(무의미)

-- ★ 1. EQUI JOIN ★
SELECT * FROM EMP, DEPT 
    WHERE ENAME='SCOTT' AND EMP.DEPTNO=DEPT.DEPTNO;

