// localStorage에서 방문자 수 가져오기
let count = localStorage.getItem('visitCount');

// 방문자 수가 없으면 0으로 초기화
if (count === null) {
    count = 0;
} else {
    // 문자열을 숫자로 변환
    count = parseInt(count);
}

// 방문자 수 1 증가
count++;

// 증가된 방문자 수를 localStorage에 저장
localStorage.setItem('visitCount', count);

// HTML 요소에 방문자 수 표시
document.getElementById('counter').textContent = count;