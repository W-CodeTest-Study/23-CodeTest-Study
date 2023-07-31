function solution(n, times) {
    var answer = 0;
    times.sort((a,b) => a-b); // 오름차순

    let left = 1;
    let right = n*times[0];

    while(left<=right){
        let mid = Math.floor((right+left)/2); // left right 의 중간
        let cnt = 0;
        for(t of times){
            cnt += Math.floor(mid/t);
            // cnt가 n보다 커지는 경우 처리
            if(cnt > n) break;
        }

        if(cnt<n){
            left = mid+1;
        }else{
            right = mid-1;
            answer = mid;
        }
    }
    return answer;
}
