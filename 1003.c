#include<stdio.h>

int idx = 1;
long arr[52][2] = {0,};
void dp(int n) {
    int i;
    if(n <= idx) return;
    for(i=idx+1;i<n+1;i++) {
        arr[i][0] = arr[i-1][0] + arr[i-2][0];
        arr[i][1] = arr[i-1][1] + arr[i-2][1];
    }
    idx = n;
}

int main() {
    int i, T, N;
    arr[0][0] = 1;
    arr[1][1] = 1;
    scanf("%d", &T);
    for(i=0;i<T;i++) {
        scanf("%d", &N);
        dp(N);
        printf("%ld %ld\n", arr[N][0], arr[N][1]);
    }

    return 0;
}