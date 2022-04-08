#include<stdio.h>
#include<stdlib.h>

struct NODE {
    int value;
    struct NODE *next;
    struct NODE *prev;
};

int len = 0;

int main() {
    int i, j, N;
    char cmd[10];
    struct NODE *head = malloc(sizeof(struct NODE));
    struct NODE *tail = malloc(sizeof(struct NODE));
    head->next = tail;
    tail->prev = head;

    scanf("%d", &N);

    for(i=0;i<N;i++) {
        scanf("%s", cmd);

        if(cmd[0]=='p'&&cmd[5]=='f') {
            scanf("%d", &j);
            struct NODE *node = malloc(sizeof(struct NODE));
            node->value = j;
            head->next = node;
            node->prev = head;
            if(len == 0) {
                tail->prev = node;
                node->next = tail;
            }
            else {
                node->next = head->next;
                head->next->prev = node;
            }
            printf("%p\n", node);
            len += 1;
        }
        else if(cmd[0]=='p'&&cmd[5]=='b') {
            scanf("%d", &j);
            struct NODE *node = malloc(sizeof(struct NODE));
            node->value = j;
            tail->prev = node;
            node->next = tail;
            if(len == 0) {
                head->next = node;
                node->prev = head;
            }
            else {
                node->prev = tail->prev;
                tail->prev->next = node;
            }
            len += 1;
        }
        else if(cmd[0]=='p'&&cmd[4]=='f') {
            if(len == 0) {
                printf("%d\n", -1);
            }
            else {
                printf("%d\n", head->next->value);
                struct NODE *tmp = head->next->next;
                printf("%p\n", head->next);
                printf("%p\n", head->next->next);
                free(head->next);
                head->next = tmp;
                head->next->prev = head;
                len -= 1;
            }
        }
        else if(cmd[0]=='p'&&cmd[4]=='b') {
            if(len == 0) {
                printf("%d\n", -1);
            }
            else {
                printf("%d\n", tail->prev->value);
                struct NODE *tmp = tail->prev->prev;
                free(tail->prev);
                tail->prev = tmp;
                tail->prev->next = tail;
                len -= 1;
            }
        }
        else if(cmd[0]=='s') {
            printf("%d\n", len);
        }
        else if(cmd[0]=='e') {
            if(len == 0) {
                printf("%d\n", 1);
            }
            else {
                printf("%d\n", 0);
            }
        }
        else if(cmd[0]=='f') {
            if(len == 0) {
                printf("%d\n", -1);
            }
            else {
                printf("%d\n", head->next->value);
            }
        }
        else if(cmd[0]=='b') {
            if(len == 0) {
                printf("%d\n", -1);
            }
            else {
                printf("%d\n", tail->prev->value);
            }
        }
    }

    return 0;
}