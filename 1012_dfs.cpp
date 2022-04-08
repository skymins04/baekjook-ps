#include<cstdio>
#include<iostream>
#include<stack>
#include<memory.h>

using namespace std;

int** arr;
int N,M;

void dfs(int x, int y) {
    int posX, posY;
    stack<int> sx;
    stack<int> sy;

    sx.push(x);
    sy.push(y);
    while(sx.size() != 0) {
        posX = sx.top();
        posY = sy.top();
        sx.pop();
        sy.pop();
        arr[posY][posX] = 0;
        if(posX != 0 && arr[posY][posX-1] == 1) {
            arr[posY][posX-1] = 0;
            sx.push(posX-1);
            sy.push(posY);
        }
        if(posX != M-1 && arr[posY][posX+1] == 1) {
            arr[posY][posX+1] = 0;
            sx.push(posX+1);
            sy.push(posY);
        }
        if(posY != 0 && arr[posY-1][posX] == 1) {
            arr[posY-1][posX] = 0;
            sx.push(posX);
            sy.push(posY-1);
        }
        if(posY != N-1 && arr[posY+1][posX] == 1) {
            arr[posY+1][posX] = 0;
            sx.push(posX);
            sy.push(posY+1);
        }
    }
}

int main() {
    int _,T,K,X,Y,i,j,cnt;

    scanf("%d",&T);
    for(_=0;_<T;_++) {
        cnt = 0;
        scanf("%d %d %d",&M,&N,&K);
        arr = new int*[N];
        for(i=0;i<N;i++) {
            arr[i] = new int[M];
            memset(arr[i], 0, sizeof(int)*M);
        }
        for(i=0;i<K;i++) {
            scanf("%d %d",&X,&Y);
            arr[Y][X] = 1;
        }

        for(i=0;i<N;i++) {
            for(j=0;j<M;j++) {
                if(arr[i][j] == 1) {
                    cnt += 1;
                    dfs(j,i);
                }
            }
        }

        printf("%d\n", cnt);


        for(i=0;i<N;i++) {
            delete arr[i];
        }
        delete arr;
    }

    return 0;
}