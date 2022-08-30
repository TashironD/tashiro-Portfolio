#include <stdio.h>

int main(void){
    int Value;
    Value=10;
    printf("%d\n",Value);

    int apple;
    int orange=10;
    apple=5;
    apple=apple+5;
    orange+=5;
    orange-=5;
    orange*=5;
    orange/=5;
    printf("%d\n",apple+orange);
    apple ++ ;
    printf("%d\n",apple);
    apple ++ ;
    printf("%d\n",apple);
    apple ++ ;
    printf("%d\n",apple);
    apple -- ;
    printf("%d\n",apple);
    return 0;
}

