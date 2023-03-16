const fs = require('fs');
const input = fs.readFileSync('./7568.txt').toString().trim().split("\n");

const [N, M] = input.shift().split(" ").map( i => Number(i));
const maps = [];
const vector = [[0,1], [1,0], [0,-1], [-1,0]];

input.forEach((i) => {
    i = i.split("").map(d => Number(d));
    maps.push(i);
});

const bfs = () => {
    const queue = [[0,0]];

    while(queue.length) {
        const cur = queue.shift();

        if(maps[cur[0]][cur[1]] !== 0) {
            const vectors = [];

            vector.forEach((v) => {
                const x = cur[0]+v[0];
                const y = cur[1]+v[1];

                if(x >= 0 && y >= 0 && x < N && y < M && maps[x][y] === 1) {
                    vectors.push([x,y]);
                }
            });

            let prev = maps[cur[0]][cur[1]];

            vectors.forEach((v) => {
                maps[v[0]][v[1]] = prev+1;
            })

            queue.push(...vectors);
        }
    }

    return maps[N-1][M-1];
}


console.log(bfs());

