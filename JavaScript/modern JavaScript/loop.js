loop: for (var i=0; i<10; i++) { // 반복문의 이름을 loop 로 설정
    for (var j=0; j<10; j++) {
        if (i === 5) {
            break loop // loop라는 이름의 반복문을 break 가장 바깥의 반복문 종료
        }
        console.log(`${i} : ${j}`)
    }
}