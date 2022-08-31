#include <stdio.h>
int main(void){

    int year = 1;
    double money = 1000000;
    while (money < 100000000){
        year++;
        money *= 1.05;
    }
    printf("%d 年目に %f 円となり、1億円を超えます。",year,money);

    return 0;
}