function solution(n, edge) {
    const map = new Array(n+1).fill().map(i => []);

    for(let i = 0 ; i < edge.length ; i++) {
        const [e1, e2] = edge[i];
        map[e1].push(e2);
        map[e2].push(e1);
    }

    const visited = new Array(n+1).fill(0);
    visited[0] = -1; // 사용하지 않는 index
    const bfs = (start) => {
        const queue = [start];

        while(queue.length) {
            console.log(queue);
            const cur = queue.shift(); // 현재 node 위치

            for(let i = 0 ; i < map[cur].length ; i++) {
                // 현재 위치의 node에서 이동가능한 다음 node가 무엇이 있는지 순회
                const next = map[cur][i];

                // next가 방문한 적 없는 node이거나,
                // visited[cur]+1 현재 노드까지 방문한 길이에 1 을 더한 것 보다 큰 경우
                if(!visited[next] || visited[next] > visited[cur] + 1) {
                    queue.push(next);
                    visited[next] = visited[cur] + 1;
                }
            }
        }
    };

    bfs(1);

    // index 0 -> 사용 X
    // index1 -> node 1임으로 제외
    visited.shift();
    visited.shift();

    const maxValue = Math.max(...visited);
    return visited.filter((el) => el === maxValue).length;
}

// 블로그 참고하여 풀음 ( 다음에 다시 풀 것 )
