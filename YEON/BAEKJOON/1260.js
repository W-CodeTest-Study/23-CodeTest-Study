const fs = require('fs');
const input = fs.readFileSync('./7568.txt').toString().trim().split("\n");
const [N, M ,V] = input.shift().split(" ").map( i => Number(i));
const graph = new Array(N+1).fill(0).map( i => []);

input.forEach((i) => {
    const [e0, e1] = i.split(" ").map( d => Number(d));

    graph[e0].push(e1);
    graph[e1].push(e0);
});



const dfs = (start) => {
    const visited = [];
    const stack = [start];

    while(stack.length) {
        const current = stack.pop();
        if(!visited.includes(current)) {
            visited.push(current);
            stack.push(...graph[current]);
        }
    }
    return visited;
}

const bfs = (start) => {
    const visited = [];
    const queue = [start];

    while(queue.length) {
        const current = queue.shift();
        if(!visited.includes(current)) {
            visited.push(current);
            queue.push(...graph[current]);
        }
    }
    return visited;
}

graph.forEach(v => v.sort((a, b) => b - a));
console.log(dfs(V).join(" "));
graph.forEach(v => v.sort((a, b) => a - b));
console.log(bfs(V).join(" "));
