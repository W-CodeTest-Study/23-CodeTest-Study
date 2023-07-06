// 시저암호
// https://school.programmers.co.kr/learn/courses/30/lessons/12926
function solution(s, n) {
    // a - z: 97~122
    // A - Z: 65~90
    var answer = [];
    s = s.split('');
    s.forEach((d) => {
        let code = d.charCodeAt();
        if(d === ' ') { answer.push(' '); }
        else if(code+n > 122 && code >= 97) {
            answer.push(String.fromCharCode(97+(code+n - 122-1)));
        }
        else if(code+n > 90 && code <= 90) {
            answer.push(String.fromCharCode(65+(code+n - 90-1)));
        }
        else {
            answer.push(String.fromCharCode(code+n));
        }
    })

    return answer.join("");
}
