#include <stdio.h>
int main (void){

    /*0か０以外か*/
    int apple = 10;
    if(apple) printf("リンゴの数は0個ではありません。\n");

    int orange = 8;
    if (orange==10) printf("orangeの数は10個です。\n");
    if (orange!=10) printf("オレンジの数は10個ではありません。\n");
    
    int suuchi;
    scanf("%d",&suuchi);
    if (suuchi < 10) printf("10未満です。");
    if (suuchi > 10) printf("10より大きいです。");
    if (suuchi == 10) printf("入力された数字は１０です。");

    int kazu;
    scanf("%d",&kazu);
    /*アンド条件　&&　*/
    if (kazu >= 5 && kazu <=10) printf("5~10の間です。");
    /*左と右のどちらか片方が真*/
    if (kazu < 5 || kazu > 10) printf("5~10の間ではありません。");
    return 0;
}