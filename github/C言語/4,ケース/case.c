#include <stdio.h>
int main(void){

    int no;
    scanf("%d",&no);
    switch (no){
    case 1:
        printf("ハリー");
        break;
    case 2:
        printf("ロン");
        break;
    case 3:
        printf("ハーマイオニー");
        break;
    case 4:
        printf("マルフォイ");
        break;
    default:
        printf("1~4のいずれかの数字を入力してください");
        break;
    }

    return 0;
}