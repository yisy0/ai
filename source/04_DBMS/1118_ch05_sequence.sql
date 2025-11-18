-- [V] Sequence : 순차번호 생성기. 대부분 인위적인 PK 사용 용도
DROP SEQUENCE FRIEND_SQ;
CREATE SEQUENCE FRIEND_SQ 
  START WITH 10 -- 1부터 생성(기본값:1)
  INCREMENT BY -1 -- 1씩 증가(기본값)
  MAXVALUE 9999 -- 최대값
  MINVALUE -9999 -- 최소값
  NOCYCLE       
  NOCACHE;      -- 캐시메모리를 사용 안 함
SELECT FRIEND_SQ.NEXTVAL FROM DUAL; -- NEXTVAL(순차번호생성), DUAL:오라클 제공 테이블(1행1열)
SELECT FRIEND_SQ.CURRVAL FROM DUAL; -- CURRVAL(현재까지 진행된 순차번호)




