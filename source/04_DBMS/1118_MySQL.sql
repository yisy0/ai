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
    sname varchar(10),
    mcode int references major(mcode)
);
insert into major (mname, moffice) values ('컴공','901호');
insert into major (mname, moffice) values ('인공지능','a601호');
select * from major;
insert into student values (101, '홍길동', 1);
insert into student values (102, '신길동', 2);
insert into student values (103, '김길동', 3);
select * from student;

-- FK(외래키) 제약조건 아래에 기술해야 함
drop table if exists major;
drop table if exists student;
create table major(
	mcode int auto_increment, -- auto_increment필드(int)
    mname varchar(10),
    moffice varchar(10),
    primary key(mcode)
);
create table student(
	sno numeric(3),
    sname varchar(10),
    mcode int ,
    primary key(sno),
    foreign key(mcode) references major(mcode) -- FK 제약조건은 아래
);
insert into major (mname, moffice) values ('컴공','901호');
insert into major (mname, moffice) values ('인공지능','a601호');
insert into major (mname, moffice) values ('빅데이터','b501호');
select * from major;
insert into student values (101, '홍길동', 1);
insert into student values (102, '신길동', 3);
insert into student values (103, '김길동', 4); -- 에러(FK제약조건)
select * from student;
-- 학번, 이름, 학과번호, 학과명, 사무실(학생 없는 학과도 출력)
select sno, sname, s.mcode, mname, moffice
	from student s right outer join major m
    on s.mcode = m.mcode;
-- -----------
-- ※ DML ※ --
-- -----------
drop table if exists personal; -- emp와 유사
drop table if exists division; -- dept와 유사
create table division(
	dno int, -- 부서번호
    dname varchar(20) not null, -- 부서명
    phone varchar(20) unique,   -- 부서전화
    position varchar(20), -- 부서위치
    primary key(dno)
);
create table personal(
	pno int, -- 사번
    pname varchar(20) not null, -- 사원명
    job   varchar(20) not null, -- 직책
    manager int,               -- 상사의 사번
    startdate date,            -- 입사일
    pay     int, -- 급여
    bonus   int, -- 상여
    dno     int, 
    primary key(pno),
    foreign key(dno) references division(dno)
);









