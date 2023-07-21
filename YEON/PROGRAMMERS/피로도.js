function solution(k, dungeons) {
    let answer = [];
    const visited = Array(dungeons.length).fill(false);

    const dfs = (depth, k) => {
        answer.push(depth);

        for(let i = 0; i < dungeons.length ; i++) {
            let current = dungeons[i];

            if(current[0] <= k && !visited[i]) {
                visited[i] = true;
                dfs(depth + 1, k - current[1]);
                visited[i] = false;
            }
        }
    }

    dfs(0, k);


    return Math.max(...answer);
}
