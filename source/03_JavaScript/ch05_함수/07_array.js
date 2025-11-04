/* array함수 : 가변인자함수 (파이썬 튜플매개변수로 구현)
 * 매개변수가 0개 : length가 0인 배열 return
 * 매개변수가 1개 : length가 매개변수만큼의 크기인 배열 return
 * 매개변수가 2개 이상 : 매개변수로 배열을 생성 return */
function array(){ // arguments(매개변수 배열) : 매개변수의 내용
  let result = [];
  if(arguments.length==1){
    // result를 argumnets[0] 만큼의 크기인 배열로 
    result.length = arguments[0];
  }else if(arguments.length >= 2){
    // result를 arguments 내용의 배열로 : result.push(arguments[0~끝까지])
    // arguments.forEach()는 불가
    for(let data of arguments){
      result.push(data);
    }
    // for(let idx in arguments){
    //   result.push(arguments[idx]);
    // }
    // for(let idx=0 ; idx<arguments.length ; idx++){
    //   result.push(arguments[idx]);
    // }
  }
  return result;
}
var arr1 = array(5);
var arr3 = Array(5);
var arr2 = array();
var arr4 = array(1, 2, 3, 99);
console.log(arr1);
console.log(arr3);
console.log(arr2);
console.log(arr4);