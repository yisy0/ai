// false로 해석되는 값 : 0, "", NaN, null, undefined  cf. []은 true
var i;
console.log(Boolean(i));
console.log(Boolean(0));
console.log(Boolean(NaN));
console.log(Boolean(Number("a")));
console.log(Boolean(""));
console.log(Boolean(null));
console.log();
console.log("0==false의 결과 :", 0==false);
console.log("0===false의 결과 :", 0===false);
// ctrl+j (터미널 창) node 파일명