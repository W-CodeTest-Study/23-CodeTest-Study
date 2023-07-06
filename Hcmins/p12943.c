#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
//재귀로도 풀고싶음
//재귀로 count변수 포인터로 넘겨서 ++해주는 방식


int solution(int num) {
    //범위가 초과해서 첨에 -1 테스트케이스에서 막혀서 더 큰 범위로 바꿈
    long number =num;
    int answer = 0;
    int result;
    
    while(number!=1){
        //짝수라면
        if(number%2==0){
            number/=2;
            answer++;
        }
        //홀수일때
        else{
            number = number*3+1;
            answer++;
        }
        printf("실행횟수 : %d, num값 : %d\n",answer,number);
        if(answer>500){
            answer=-1;
            break;
        }
    }
    
    
    return answer;
}
