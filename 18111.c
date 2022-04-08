#include<stdio.h>
#include<stdlib.h>

int main() {
    int i, j, del, cre, N, M, B, min = 9999, max = -9999, offset, time = 500*500*256*2+1, height;
    scanf("%d %d %d", &N, &M, &B);

    int** arr = (int**)malloc(sizeof(int*) * N);
    for(i=0;i<N;i++) arr[i] = (int*)malloc(sizeof(int) * M);

    for(i=0;i<N;i++) {
        for(j=0;j<M;j++) {
            scanf("%d", &arr[i][j]);
            if(min > arr[i][j]) min = arr[i][j];
            if(max < arr[i][j]) max = arr[i][j];
        }
    }
    height = max;

    for(offset=max;offset>min-1;offset--) {
        del = 0;
        cre = 0;
        for(i=0;i<N;i++) {
            for(j=0;j<M;j++) {
                if(arr[i][j] > offset) {
                    del += (arr[i][j] - offset)*2;
                }
                else if(arr[i][j] < offset) {
                    cre += offset - arr[i][j];
                }
            }
        }
        if((cre-del/2) <= B && time > cre+del) {
            time = cre+del;
            height = offset;
        }
    }

    printf("%d %d", time, height);

    return 0;
}