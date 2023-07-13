// https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=javascript

function solution(park, routes) {
    const DIRECTION = {
        'N': -1,
        'S': 1,
        'E': 1,
        'W': -1,
    };

    const W = park[0].length;
    const H = park.length;

    var answer = [];
    const map = [];
    let start = [0,0];

    // 1. park를 2차원 배열 형태로 변경
    park.forEach((p, index) => {
        const m = p.split("");

        // 2. 시작 인덱스 저장
        if(m.includes('S')) {
            start[0] = index;
            start[1] = m.indexOf('S');
        }

        map.push(m);
    });

    // 로봇의 현재 위치
    let current = start;

    // 경로 순서대로 읽음
    routes.forEach((r) => {
        const [dir, num] = r.split(' ');
        let flag = true;

        // 로봇의 예상 위치
        // deepcopy 해줘야 함.
        let expect = [...current];

        if(dir === 'N' || dir === 'S') {
            // 위아래 이동
            // expect[0]
            for(let i = 0 ; i < Number(num) ; i++) {
                expect[0] += DIRECTION[dir];
                if(expect[0] >= H || expect[0] < 0 || map[expect[0]][expect[1]] === 'X') {
                    flag = false;
                    break;
                }
            }
        } else {
            // 오른쪽 왼쪽 이동
            // expect[1]
            for(let i = 0 ; i < Number(num) ; i++) {
                expect[1] += DIRECTION[dir];
                if(expect[1] >= W || expect[1] < 0 || map[expect[0]][expect[1]] === 'X') {
                    flag = false;
                    break;
                }
            }
        }

        if(flag) {
            current = expect;
        }
    });

    return current;
}
