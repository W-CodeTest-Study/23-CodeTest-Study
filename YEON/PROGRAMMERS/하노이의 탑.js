const arr=[];

function solution(n) {
    dp(n,1,3,2);

    return arr;
}

function dp(n,src,dst,mid){
    if(n==1){
        arr.push([src,dst]);
    }
    else{
        dp(n-1,src,mid,dst); // A -> B
        arr.push([src,dst]); // A -> C
        dp(n-1,mid,dst,src); // B -> C
    }

}
