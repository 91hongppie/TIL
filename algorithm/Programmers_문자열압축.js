function solution(s) {
    var answer = 0;
    for (var i=1, tempAnswer=''; i<s.length/2+1; i++) {
        var j = 0
        for (var j=0, count=1; j<=s.length; j+=i) {
            if (s.slice(j, j+i) === s.slice(j+i, j+i+i)) {
                count += 1
            } else {
                if (count === 1) {
                    tempAnswer += s.slice(j, j+i)
                } else {
                    tempAnswer += count.toString() + s.slice(j, j+i)
                    count = 1
                }
            }
        }
        if (answer === 0) {
            answer = tempAnswer.length
        } else {
            if (answer > tempAnswer.length) {
                answer = tempAnswer.length
            }
        }
        tempAnswer = ''
    }
    return answer;
}