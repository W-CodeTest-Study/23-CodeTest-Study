// https://school.programmers.co.kr/learn/courses/30/lessons/12943
// 콜라츠 추측

function solution(num) {
    let answer = 0;

    while(answer < 501 && num !== 1 ){
        if(num % 2 === 0) {
            num = num / 2;
            answer+=1;
        }else{
            num = (num * 3) + 1;
            answer+=1;
        }
    }

    return answer > 500 ? -1 : answer;
}
