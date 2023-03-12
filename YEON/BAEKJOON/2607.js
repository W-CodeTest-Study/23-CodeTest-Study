const fs = require('fs');
let input = fs.readFileSync('./7568.txt').toString().trim().split("\n");

const N = Number(input.shift());
const STRING = input.shift();
const stringDic = {};
STRING.split("").forEach((s) => {
    if(stringDic[s] === undefined) {
        stringDic[s] = 1;
    } else {
        stringDic[s]++;
    }
});

const strArr = input;
let answer = 0;

// 문자가 구성을 갖는지 확인하는 함수
const sameWord = (str) => {
    let string = STRING.split("").sort().join("");
    str = str.split("").sort().join("");
    return string === str;
}

strArr.forEach((s) => {
    // 기준이 되는 단어보다 비교하는 단어의 길이가 1 작은 경우
    let string = STRING.split("").sort();
    let compare = s.split("").sort();

    for(let i = 0 ; i < string.length ; i++) {
        for(let j = 0 ; j < compare.length ; j++) {
            if(compare[j] === string[i]) {
                string[i] = '';
                compare[j] = '';
            }
        }
    }
    string = string.filter((s) => s !== '');
    compare = compare.filter((s) => s !== '');
   // 기준이 되는 단어와 비교하는 단어의 길이는 최대 1까지 차이 날 수 있다.
   if(s.length === STRING.length) {
       // 기준이 되는 단어와 비교하는 단어의 길이가 같은 경우
       if(sameWord(s)) {
           answer++;
       } else {
           if(string.length === 1 && compare.length === 1) {
               answer++;
           }
       }
   } else if(s.length +1 === STRING.length ) {
       if(string.length === 1 && compare.length === 0) {
           answer++;
       }
   } else if(s.length -1 === STRING.length ) {
       // 기준이 되는 단어보다 비교하는 단어의 길이가 1 큰 경우
       if(string.length === 0 && compare.length === 1) {
           answer++;
       }
   } else {
       // 그 외는 같은 구성의 단어가 될 수 없음.
   }
});

console.log(answer);
