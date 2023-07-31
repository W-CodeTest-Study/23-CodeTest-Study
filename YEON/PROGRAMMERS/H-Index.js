function solution(citations) {

    // 내림차순 정렬
    citations.sort( (a,b) => {
        return b - a;
    });

    for( let i = 0 ; i < citations.length ; i ++){
        let h_index = i + 1;
        if( citations[i] < h_index){
            return h_index - 1;
        }

        if( citations[i] === h_index){
            return h_index;
        }

        if( h_index === citations.length ){
            return h_index;
        }
    }
}
