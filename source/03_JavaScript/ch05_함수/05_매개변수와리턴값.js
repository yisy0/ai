console.log(pow(5, 3));

function pow(x, y){
  let result = 1;
  for(let cnt=1 ; cnt<=y ; cnt++){
    result *= x; // result = result*x;
  }
  return result;
}