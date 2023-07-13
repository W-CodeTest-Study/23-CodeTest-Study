#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=c


// park_len은 배열 park의 길이입니다.
// routes_len은 배열 routes의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* park[], size_t park_len, const char* routes[], size_t routes_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*2);
    //첫 위치 저장
    int h = (int)park_len;
    int w;
    char op;
    int n;
    
    int current_h;
    int current_w;
    int temp_h;
    int temp_w;
    
    for(w=0;w<50;w++){
        if(park[0][w]=='\0')
            break;
    }
    
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            
            if(park[i][j]=='S'){
                current_h=i;
                current_w=j;
            }
        }
    }
    printf("%d %d",current_h,current_w);
    for(int i=0;i<routes_len;i++){
        int j;
        op=routes[i][0];
        n=routes[i][2]-48;
        temp_h=current_h;
        temp_w=current_w;
        switch(op){
            case 'N':
                for(j=0;j<n;j++){
                    temp_h--;
                    if(temp_h<0||temp_h>h-1){
                  
                        break;
                    }
                    
                    if(park[temp_h][temp_w]=='X'){
                      
                        break;
                    }
                }
                if(j==n)
                    current_h=temp_h;
                break;
            case 'S':
                for(j=0;j<n;j++){
                    temp_h++;
                    if(temp_h<0||temp_h>h-1){
                      
                        break;
                    }
                    if(park[temp_h][temp_w]=='X'){
                    
                        break;
                    }
                }
                if(j==n)
                    current_h=temp_h;
                
                break;
            case 'W':
                for(j=0;j<n;j++){
                    temp_w--;
                    if(temp_w<0||temp_w>w-1){
                       
                        break;
                    }
                    if(park[temp_h][temp_w]=='X'){
                        
                        break;
                    }
                }
                if(j==n)
                    current_w=temp_w;
                break;
            case 'E':
                for(j=0;j<n;j++){
                    temp_w++;
                    if(temp_w<0||temp_w>w-1){
                      
                        break;
                    }
                    if(park[temp_h][temp_w]=='X'){
                       
                        break;
                    }
                }
                if(j==n)
                    current_w=temp_w;
                break;
        }
        
    }
    
    answer[0]=current_h;
    answer[1]=current_w;
    
   
    return answer;
}