// 2.js:동적인부분(utf-8)
name = prompt("이름은?", "홍길동");  // 취소를 클릭시 'null' 리턴
if (name != 'null') {
    document.write(name + '님 반갑습니다<br>');
}