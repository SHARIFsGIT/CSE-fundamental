#include<stdio.h>

int main(){
    int money;
    scanf("%d", &money);

    if(money>10000){
        printf("Gucci Bag");
        if(money>20000){
            printf("\nGucci Belt");
        }
    }
    else if(money>5000){
        printf("Levis Bag");
    }
    else{
        printf("Something");
    }
    return 0;
}
