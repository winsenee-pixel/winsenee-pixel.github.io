// 시계 관련 코드 (기존 방문자 카운터 코드 위에 추가)
function updateClock() {
    const now = new Date();
    let hours = now.getHours().toString().padStart(2, '0');
    let minutes = now.getMinutes().toString().padStart(2, '0');
    let seconds = now.getSeconds().toString().padStart(2, '0');
    
    const digits = document.querySelectorAll('#nixie-clock .digit');
    
    digits[0].textContent = hours[0];
    digits[1].textContent = hours[1];
    digits[2].textContent = minutes[0];
    digits[3].textContent = minutes[1];
    digits[4].textContent = seconds[0];
    digits[5].textContent = seconds[1];
}

// 1초마다 시계 업데이트
setInterval(updateClock, 1000);

// 페이지 로드 시 바로 시계 업데이트
updateClock();


// --- 기존 방문자 카운터 코드 ---
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