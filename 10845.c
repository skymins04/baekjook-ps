#include<stdio.h>
#include<stdlib.h>

struct NODE {
    int value;
    char isHead;
    char isTail;
    struct NODE *next;
    struct NODE *prev;
};

int len = 0;

int main() {
    int N, i, j;
    char cmd[5];
    struct NODE *head = malloc(sizeof(struct NODE));
    struct NODE *tail = malloc(sizeof(struct NODE));
    struct NODE *crnt = malloc(sizeof(struct NODE));
    head->next = tail;
    head->isHead = 1;
    tail->prev = head;
    tail->isTail = 1;
    crnt->next = head->next;

    scanf("%d", &N);
    
    for(i=0;i<N;i++) {
        scanf("%s", cmd);
        if(cmd[0] == 'p' && cmd[1] == 'u') {
            len += 1;
            scanf("%d", &j);
            struct NODE *node = malloc(sizeof(struct NODE));
            node->value = j;
            node->next = tail;
            node->prev = tail->prev;
            if(len == 1) {
                head->next = node;
            }
            else {
                tail->prev->next = node;
            }
            tail->prev = node;
        }
        else if(cmd[0] == 'p') {
            if(len == 0) {
                printf("%d\n", -1);
            }
            else {
                len -= 1;
                printf("%d\n", head->next->value);
                printf("%p\n", head->next);
                printf("%p\n", head->next->next);
                struct NODE *tmp = head->next->next;
                free(head->next);
                head->next = tmp;
            }
        }
        else if(cmd[0] == 'f') {
            if(len == 0) {
                printf("%d\n", -1);
            }
            else {
                printf("%d\n", head->next->value);
            }
        }
        else if(cmd[0] == 'b') {
            if(len == 0) {
                printf("%d\n", -1);
            }
            else {
                printf("%d\n", tail->prev->value);
            }
        }
        else if(cmd[0] == 's') {
            printf("%d\n", len);
        }
        else if(cmd[0] == 'e') {
            if(len == 0) {
                printf("%d\n", 1);
            }
            else {
                printf("%d\n", 0);
            }
        }
    }

    return 0;
}