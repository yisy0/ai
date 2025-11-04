/* array함수 : 가변인자함수 (파이썬 튜플매개변수로 구현)
 * 매개변수가 0개 : length가 0인 배열 return
 * 매개변수가 1개 : length가 매개변수만큼의 크기인 배열 return
 * 매개변수가 2개 이상 : 매개변수로 배열을 생성 return */
function array(){ // arguments(매개변수 배열) : 매개변수의 내용
  console.log('매개변수 개수 :', arguments.length);
  console.log(arguments);
}
array(1, '이', 3, true, false);