/**
 * 문제유형: 스택/큐
 * 난이도: lv2
 * 언어: JS
 * https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=javascript
 **/
function solution(bridge_length, weight, truck_weights) {
    const bridge = new Array(bridge_length).fill().map((v) => 0);

    let time = 0; // 시간
    let bridge_weight = 0 // 현재 다리 위에 있는 트럭의 무게
    let truck_number = truck_weights.length; // 다리를 건너지 못한 트럭의 갯수

    // 다리를 건너지 못한 트럭의 갯수가 0보다 큰동안 while문 돌리기
    // 다 건넜으면 time return
    while(truck_number > 0) {
        // time 증가
        time++;

        // 현재 다리 위의 트럭의 무게 구하기
        bridge_weight = bridge.reduce((partialSum, a) => partialSum + a, 0);

        // 만약 다리 위에 트럭의 무게가 다리의 최대 무게보다 작거나 같으면서
        // 다리 위에 트럭의 무게 + 대기중인 트럭 무게가 최대 무게보다 작거나 같으면
        // 대기중인 트럭 다리 위로 올림
        if(bridge_weight <= weight
            && bridge_weight + truck_weights[0] <= weight) {
            let b = bridge.shift();
            if(b > 0) truck_number--;
            bridge.push(truck_weights.shift());
        } else if(bridge_weight <= weight
            && bridge_weight + truck_weights[0] > weight) {
            // 다리 위에 트럭의 무게 + 대기중인 트럭 무게가 최대 무게보다 크면
            // 그냥 다리 위에 있는 트럭만 이동
            // 이때 트럭이 다리 다 건너면 truck number --;
            let b = bridge.shift();
            if(b > 0) truck_number--;
            // 다리 위에 트럭의 무게 다시 계산
            bridge_weight = bridge.reduce((partialSum, a) => partialSum + a, 0);
            if(bridge_weight <= weight
                && bridge_weight + truck_weights[0] <= weight) {
                bridge.push(truck_weights.shift());
            } else bridge.push(0);
        } else if(bridge_weight <= weight && truck_weights.length === 0){
            let b = bridge.shift();
            if(b > 0) truck_number--;
            bridge.push(0);
        }
    }
    return time;
}
