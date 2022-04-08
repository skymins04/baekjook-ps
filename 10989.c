#include<stdio.h>

int main(void) {
    int i, j, N, cnt[10001] = {0};
    scanf("%d", &N);
    for(i=0;i<N;i++) {
        scanf("%d",&j);
        cnt[j]+=1;
    }
    for(i=0;i<10001;i++) {
        for(j=0;j<cnt[i];j++) {
            printf("%d\n", i);
        }
    }
    return 0;
}