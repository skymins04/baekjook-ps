#include<stdio.h>
#include<math.h>

void fs(int n) {
    int tmp=0,i,j,k,g;
    for(i=floor(pow(n,0.5));i>-1;i--) {
        tmp+=i*i;
        if(tmp==n) {
            printf("1");
            return;
        }
        else if(i!=0) {
            for(j=i;j>-1;j--) {
                tmp+=j*j;
                if(tmp==n) {
                    printf("2");
                    return;
                }
                else if(j!=0) {
                    for(k=j;k>-1;k--) {
                        tmp+=k*k;
                        if(tmp==n) {
                            printf("3");
                            return;
                        }
                        else if(k!=0) {
                            for(g=k;g>-1;g--) {
                                tmp+=g*g;
                                if(tmp==n) {
                                    printf("4");
                                    return;
                                }
                                tmp-=g*g;
                            }
                        } 
                        tmp-=k*k;
                    }
                }
                tmp-=j*j;
            }
        }
        tmp-=i*i;
    }
}

int main() {
    int N;
    scanf("%d",&N);
    fs(N);
    return 0;
}