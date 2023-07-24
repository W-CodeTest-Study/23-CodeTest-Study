function solution(begin, target, words) {
    var answer = 0;

    // 입출력 예시 2
    // words에 target 포함 안된 경우 return 0
    if(!words.includes(target)) {
        return 0;
    }

    const visited = [];
    const queue = [];

    queue.push([begin, answer]);

    while(queue) {
        let [current, cnt] = queue.shift();

        if (current === target) {
            return cnt;
        }

        words.forEach(word => {
            let different = 0; // 1이면 한 단어만 다른 문자

            if(visited.includes(word)) return;

            // 다른 단어 갯수 구하기
            for (let i=0; i<word.length; i++) {
                if (word[i] !== current[i]) different++;
            }

            // 다른 단어 갯수 1 이면 큐에 단어, 횟수로 넣음
            if (different === 1) {
                queue.push([word, ++cnt]);
                visited.push(word);
            }
        });
    }

    return answer;
}
