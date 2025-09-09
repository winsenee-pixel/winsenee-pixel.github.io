// localStorage에서 방문자 수 가져오기
let count = localStorage.getItem('visitCount');

// localStorage에서 방문 여부 확인
let hasVisited = localStorage.getItem('hasVisited');

// 방문자 수가 없으면 0으로 초기화
if (count === null) {
    count = 0;
} else {
    // 문자열을 숫자로 변환
    count = parseInt(count);
}

// 이전에 방문한 기록이 없으면
if (hasVisited === null) {
    // 방문자 수 1 증가
    count++;
    // 방문 기록을 남김 (값은 아무거나 상관없음)
    localStorage.setItem('hasVisited', 'true');
    // 증가된 방문자 수를 localStorage에 저장
    localStorage.setItem('visitCount', count);
}

// HTML 요소에 방문자 수 표시
document.getElementById('counter').textContent = count;