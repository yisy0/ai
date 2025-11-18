-- DCL(계정 생성, 권한부여, 권한박탈, 계정삭제)
-- DDL(제약조건 FK, 시퀀스없음)
-- DML(and:&&, or:||, 연결연산자대신concat사용, outer join)

-- -----------
-- ※ DCL ※ --
-- -----------
create user user01 identified by 'password';
grant all privileges on *.* to user01; -- 권한부여
drop user user01; -- 계정삭제

-- -----------
-- ※ DDL ※ --
-- -----------
-- 기존 데이터베이스들(스키마)
show databases;
create database devdb; -- 새로운 데이터베이스(스키마) devdb 생성
use devdb; -- devdb 데이터베이스로 들어감
select database(); -- 현재 들어와 있는 데이터베이스
show tables; -- 현재 데이터베이스 내의 테이블
create table emp(
	empno numeric(4) primary key, -- 숫자4자리
    ename varchar(6) not null, -- 6글자
    nickname varchar(6) unique,
    sal   numeric(7, 2) check(sal>0),
    comm  numeric(7,2) default 0
);
/* MySQL타입 : numeric(n, d), varchar(n), date
정수 : tinyint(1byte), smallint(2byte) mediumint(3byte)
      int/integer(4byte) bigint(8byte)
실수 : float(n, d;4byte), double(n,d;8byte)
문자 : char(n), text, mediumtext(16M), longtext(4GB)
날짜 : date, datetime, time
*/
desc emp;
insert into emp (empno, ename, nickname, sal)
	values (1111, '홍길동번쩍이', '동해번쩍쩍쩍', 9000);
select empno "no", ename 이름, nickname 별명, sal, comm from emp;

-- 시퀀스 대체, FK제약조건 
-- major(mcode시퀀스, mname, moffice)/student(sno, sname, mcode:FK)
-- set @@auto_increment_increment=10 
create table major(
	mcode int primary key auto_increment, -- auto_increment필드(int)
    mname varchar(10),
    moffice varchar(10)
);
create table student(
	sno numeric(3) primary key,
);





