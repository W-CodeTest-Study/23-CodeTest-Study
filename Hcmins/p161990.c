#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

//https://school.programmers.co.kr/learn/courses/30/lessons/161990


// wallpaper_len은 배열 wallpaper의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* wallpaper[], size_t wallpaper_len) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*4);
    int h=wallpaper_len;
    int w;
    int num_file=0;
    for(w=0;w<50;w++){
        if(wallpaper[0][w]=='\0'){
            break;
        }
    }
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            if(wallpaper[i][j]=='#')
                num_file++;
        }
    }
    int files[num_file][2];
    // files 배열은 파일의 x,y가 담겨있다.
    int k=0;
    for(int i=0;i<h;i++){
        for(int j=0;j<w;j++){
            if(wallpaper[i][j]=='#'){
                files[k][0]=i;
                files[k][1]=j;
                k++;
            }
        }
    }
    //최대x,y answer[2],answer[3]
    for(int i=0;i<2;i++){
        int max=0;
        
        for(int j=0;j<num_file;j++){
            if(max<files[j][i]){
                max=files[j][i];
            }
        }
        answer[i+2]=max+1;
    }
    //최소 x,y answer[0],answer[1]
    
    for(int i=0;i<2;i++){
        int min;
        if(h>w){
            min=h;
        }
        else{
            min=w;
        }
        for(int j=0;j<num_file;j++){
            if(min>files[j][i]){
                min=files[j][i];
            }
        }
        answer[i]=min;
    }
    for(int i=0;i<4;i++){
        printf("%d",answer[i]);
    }
    return answer;
}