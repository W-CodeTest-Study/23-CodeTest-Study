const fs = require('fs');
const input = fs.readFileSync('./7568.txt').toString().trim().split("\n");
const vector = [[1,0], [-1,0], [0,1], [0,-1]];

let cnt = 0;

const N = Number(input.shift());
const maps = input.map((i) => {
   i = i.split("").map(d => Number(d));
   return i;
});

const dfs = (start) => {
    const stack = [start];

    let cnt = 0;
    while(stack.length) {
        const cur = stack.pop();
        if(maps[cur[0]][cur[1]]) {
            maps[cur[0]][cur[1]] = 0;
            cnt++;
            const vectors = [];
            vector.forEach((v) => {
                if(v[0]+cur[0] >= 0 && v[0]+cur[0] < maps.length && v[1]+cur[1] >= 0 && v[1]+cur[1] < maps[0].length) {
                    vectors.push([v[0]+cur[0], v[1]+cur[1]]);
                }
            });
            stack.push(...vectors);
        }
    }
    return cnt;
}

let answer = 0;
let answerArr = [];

for(let i = 0; i < maps.length ; i++) {
    for(let j = 0 ; j < maps[0].length ; j++) {
        const result = dfs([i,j]);
        if(result) {
            answer++;
            answerArr.push(result);
        }
    }
}

answerArr = answerArr.sort(function(a,b) {
    return a - b;
});
console.log(answer);
for(let i = 0 ; i < answer ;i ++) {
    console.log(answerArr[i]);
}
