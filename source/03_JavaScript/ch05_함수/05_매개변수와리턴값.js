console.log(pow(5, 3));
// 선언된 매개변수보다 많은 매개변수로 호출될 경우 : 뒷부분 무시
console.log(pow(5, 2, 1, 10));
// 선언된 매개변수보다 적은 매개변수로 호출될 경우 : 전달되지 않은 매개변수는 undefined
console.log(pow(5));
function pow(x, y){
  let result = 1;
  for(let cnt=1 ; cnt<=y ; cnt++){
    result *= x; // result = result*x;
  }
  return result;
}