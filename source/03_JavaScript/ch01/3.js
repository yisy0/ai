/* 변수선언시 var(전역변수), let(지역변수), const(상수) */
// var : 변수의 재선언 가능. 전역변수로 사용(한 파일 전체 scope 적용)
// let : 변수의 재선언 불가. 지역변수로 사용(선언된 블록 scope 적용)
// const : 새로운 값을 재할당 할 수 없음.
let sum = 0;
for(var i=1 ; i<=10 ; i++){
  sum += i; // sum = sum+i
  console.log('i = ' + i + "일때까지 누적된 합은 " + sum);
}
console.log('for문 끝난 후 i값은', i);
//실행 터미널(ctrl+j)에서 node 3.js실행