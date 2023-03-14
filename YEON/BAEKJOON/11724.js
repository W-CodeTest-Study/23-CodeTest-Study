const fs = require('fs');
const input = fs.readFileSync('./7568.txt').toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map( i => Number(i));
const graph = new Array(N+1).fill(0).map(i => []);
let V = new Array(N+1).fill(false);

input.forEach((i) => {
    const [to, from] = i.split(" ").map(n => Number(n));
    graph[to].push(from);
    graph[from].push(to);
});

const dfs = (start) => {
    const visited = [];
    let stack = [start];

    while(stack.length) {
        const cur = stack.pop();
        if(!visited.includes(cur)) {
            visited.push(cur);
            V[cur] = true;
            stack.push(...graph[cur]);
            graph[cur].length = 0;
        }
    }
    return visited;
}

let start = 1;
let cnt = 0;

while(start !== graph.length) {
    if(graph[start].length) {
        dfs(start);
        cnt++;
    }
    start++;
}

V = V.filter(v => !v); // 혼자 있는 vertex 고려
console.log(V.length > 1 ? cnt+V.length-1 : cnt);
