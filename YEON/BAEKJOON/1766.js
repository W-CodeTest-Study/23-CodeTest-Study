const fs = require('fs');
const input = fs.readFileSync('./7568.txt').toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map(n => Number(n));
const graph = new Array(N+1).fill(0).map(i => []);
const indegree = new Array(N+1).fill(0);

for(let i = 0 ; i < M ; i++) {
    const [to, from] = input[i].split(' ').map(n => Number(n));
    graph[to].push(from);
    indegree[from]++;
}

const tOrder = [];
const queue = [];

// indegree 0 인거 찾아서 큐에 추가
for(let i = 1; i < graph.length ; i ++) {
    if(indegree[i] === 0) {
        queue.push(i);
        break;
    }
}

while(queue.length) {
    const node = queue.shift();
    indegree[node] = -1; // 다시 안찾게 -1

    const targetNode = graph[node]; // 현재 node가 가리키고있는 다른 node들 리스트
    // indegree 낮춰주기
    targetNode.forEach((i) => {
       indegree[i]--;
    });
    tOrder.push(node);

    // indegree 0인거 앞에서부터 찾기
    for(let i = 1; i < graph.length ; i ++) {
        if(indegree[i] === 0) {
            queue.push(i);
            break;
        }
    }
}

console.log(tOrder.join(" "))

