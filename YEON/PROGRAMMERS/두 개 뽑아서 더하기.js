function solution(numbers) {
    answer = new Set();

    for(let i = 0 ; i < numbers.length ; i++){
        for( let j = i ; j < numbers.length ; j++){
            if( i !== j){
                answer.add(numbers[i]+numbers[j]);
            }
        }
    }
    answer = Array.from(answer);
    answer.sort(function(a,b){
        return a - b;
    })

    return answer;
}
