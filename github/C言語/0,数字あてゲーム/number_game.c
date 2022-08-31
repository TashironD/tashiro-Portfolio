#include <stdio.h>/*文字列を出力するため*/
#include <stdlib.h>/*C言語の標準ヘッダ*/

/*一番最初に実行されるメイン関数*/
int main(void){
    /*必要な変数たちの宣言*/
    int num;/*プレイヤーが入力した数字*/
    int ans = rand() % 51;/*PCが指定する0~50の数字*/
    int max_try = 5;/*プレイヤーの最大回答回数*/
    int remain = max_try;/*プレイヤーの残りの解答回数*/

    do{
        printf("数値は何ですか？");
        scanf("%d",&num);/*プレイヤーの回答をnumに入れる*/
        remain --;/*回答回数が１減る*/
        if (num > ans) printf("もっと小さいです。");
        if (num < ans) printf("もっと大きいです。");
    }while(num != ans && remain > 0);/*numとansが一致しない且つremainが０より大きい場合繰り返す*/

    if (num != ans)
        printf("残念。正解は%dでした。またチャレンジしてね！",ans);
    else{
        printf("おめでとう！正解です。");
        printf("%d回で正解しました。",max_try - remain);
    }
}