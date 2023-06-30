function solution(maps) {
    var answer = 0;
    // 상 하 좌 우
    const vector = [[-1, 0], [1, 0], [0, -1], [0, 1]];

    // bfs
    const bfs = () => {
        const queue = [[0,0]];

        while(queue.length) {
            const cur = queue.shift();
            if(maps[cur[0]][cur[1]] !== 0) {
                const vectors = [];

                vector.forEach((v) => {
                    const x = Number(cur[0])+ Number(v[0]);
                    const y = Number(cur[1])+ Number(v[1]);

                    if(x >= 0 && y >= 0 && x < maps.length && y < maps[0].length && maps[x][y] === 1) {
                        vectors.push([x,y]);
                    }
                });

                const prev = maps[cur[0]][cur[1]];

                vectors.forEach((v) => {
                    maps[v[0]][v[1]] = prev+1;
                });
                queue.push(...vectors);
            }
        }
    }

    bfs();
    // [N-1][M-1] 위치값이 1 이면 도달 못하는 것이기 때문에 -1
    return maps[maps.length-1][maps[0].length-1] === 1 ? -1 : maps[maps.length-1][maps[0].length-1];
}
