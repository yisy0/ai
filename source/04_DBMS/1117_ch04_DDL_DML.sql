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
CREATE TABLE BOOK(
  BOOKID NUMBER(4), -- BOOKID필드의 타입은 숫자4자리
  BOOKNAME VARCHAR2(20), 
);










