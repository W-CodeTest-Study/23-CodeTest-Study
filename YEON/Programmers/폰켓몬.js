/**
 * 문제유형: 해시
 * 난이도: lv1
 * 언어: JS
 * 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=javascript
 */

function solution(nums) {
    const hash = {};

    nums.forEach((n) => {
        if(hash[n] === undefined) hash[n] = 1;
        else hash[n] += 1;
    });

    const M = nums.length/2; // 선택할 수 있는 수
    const keyList = Object.keys(hash); // 폰켓몬 종류 수

    // 선택할 수 있는 수 >= 폰켓몬 종류 수 -> 폰켓몬 종류수
    // 선택할 수 있는 수 < 폰켓몬 종류 수 -> 선택할 수 있는 수
    return M >= keyList.length ? keyList.length : M;
}
