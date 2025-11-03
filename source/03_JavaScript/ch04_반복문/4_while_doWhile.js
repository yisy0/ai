// 1초동안 반복하는 while 구문 / do~while 구문
var cnt = 0; // 반복횟수
var startTime = new Date().getTime(); // 시작시점의 밀리세컨
// while(new Date().getTime() <= startTime + 1000){
//   cnt++; // cnt 1증가
// }
do{
  cnt++;
}while(new Date().getTime() <= startTime + 1000);
console.log('1초동안 while문 수행한 횟수 :',cnt);