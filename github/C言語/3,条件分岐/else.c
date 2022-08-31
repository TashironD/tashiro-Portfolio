#include <stdio.h>
int main(void){

    int suuchi;
    scanf("%d",&suuchi);
    if (suuchi == 10)
        printf("10と同じです。");
    else
        printf("10ではありません。");


    int age;
    scanf("%d",&age);
    if (age <= 3){
        printf("0円です。");
    }else if(age <= 20){
        printf("1000円です。");
    }else{
        printf("1500円です。");
    }
    return 0;
}