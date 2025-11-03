let num1 = 30;
let num2 = 21;
let difference = (num1>num2) ? num1-num2 : num2-num1;
if(num1>num2){
  msg = '첫번째 수가 '+ difference +'만큼 더 크다';
}else if(num2> num1){
  msg = '두번째 수가 '+ difference +'만큼 더 크다';
}else{
  msg = '두 수는 같다';
}
console.log(msg);