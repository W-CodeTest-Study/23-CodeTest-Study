function solution(priorities, location) {
    // priorities 중요도
    // location 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지 알려주는 변수
    // answer 내가 요청한 문서가 몇 번째로 인쇄되는지 return

    let printed = 0;
    priorities = priorities.map((p,index) => {
        if(index === location) return {prio: p, target: true};
        return {prio: p, target: false};
    });

    while(true) {
        const arr = priorities.map(p => {
            return p.prio;
        });
        let max = Math.max(...arr);

        if(priorities[0]['prio'] !== max) {
            let prio = priorities.shift();
            priorities.push(prio);
        } else {
            if(priorities[0]['target'] === true) {
                return ++printed;
            }
            priorities.shift();
            printed++;
        }
    }
}
