#include<stdint.h>

int main(){
    int num;
    scanf("%d", &num);
    if(num == 0){
        printf("zero");
    }
    else if(num<0){
        printf("negative");
    }
    else{
        printf("positive");
    }
    return 0;
}
