/* do while分は、条件式を処理の後ろに記述しているため必ず１回は処理が行われる*/
#include <stdio.h>
int main(void){

    int i = 10;
    while (i <5){
        printf("while文です。\n");
    }
    do{
        printf("do while文です。");
    }while(i < 5);
    
    return 0;
}