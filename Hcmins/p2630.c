#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


//재귀
// 첨에는 dfs식으로 재귀로 계속들어가서 작은것쪽부터 큰쪽으로 확인할려했는데 이러면 색종이 개수 못새서 bfs식으로 바꿈
// 우선 큰거 확인하고 파란종이인지 흰종이인지 먼저 체크하고 둘다 아니면 그때 4개로 쪼개서 다시 확인 이렇게 재귀
void check (int** map,int x,int y, int N,int* ptr_blue, int *ptr_white);

int main(){
    
    int N;
    int ** map;
    int num_blue=0;
    int num_white=0;
    
    scanf("%d",&N);

    map=(int**)malloc(sizeof(int*)*N);
    for(int i=0;i<N;i++){
        map[i]=(int*)malloc(sizeof(int)*N);
    }
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            scanf("%d",&map[i][j]);
        }
    }
    
    check(map,0,0,N,&num_blue,&num_white);
    
    printf("%d\n",num_white);
    printf("%d\n",num_blue);

}
//dfs로 접근했는데 종이 수를 구하는게 막힘 -> bfs식 접근
void check (int** map,int x,int y, int N,int* ptr_blue, int *ptr_white){
    
    // 파란종이인지 확인
    int num=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(map[x+i][y+j]==1){
                num++;
            }
        }
    }
    if(num==N*N){
        *ptr_blue+=1;
        return ;
    }
    //흰종이인지 확인
    num=0;
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            if(map[x+i][y+j]==0){
                num++;
            }
        }
    }
    if(num==N*N){
        *ptr_white+=1;
        return;
    }

    //섞여있으면(파란종이,흰종이도 아니면) 재귀 이때 4개로 쪼개고 각각 다시 이거 돌림
    check(map,x,y,N/2,ptr_blue,ptr_white);
    check(map,x+N/2,y,N/2,ptr_blue,ptr_white);
    check(map,x,y+N/2,N/2,ptr_blue,ptr_white);
    check(map,x+N/2,y+N/2,N/2,ptr_blue,ptr_white);

}