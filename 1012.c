#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int** arr;

int main() {
    int _, T, N, M, K, X, Y, i, j, cnt;
    scanf("%d", &T);
    for(_=0;_<T;_++) {
        scanf("%d %d %d", &M, &N, &K);
        arr = (int**)malloc(sizeof(int*)*N);
        for(i=0;i<N;i++) {
            arr[i] = (int*)calloc(M, sizeof(int));
        }  
        for(i=0;i<K;i++) {
            scanf("%d %d", &X, &Y);
            arr[Y][X] = 1;
        }

        for(i=0;i<N;i++) {
            for(j=0;j<M;j++) {
                if(arr[i][j])
            }
        }

        for(i=0;i<N;i++) {
            for(j=0;j<M;j++) {
                printf("%d ", arr[i][j]);
            }
            printf("\n");
        }


        for(i=0;i<N;i++) {
            free(arr[i]);
        }
        free(arr);
    }
    return 0;
}