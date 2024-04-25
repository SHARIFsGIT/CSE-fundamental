#include <stdio.h>

int main() {
    int T;
    scanf("%d", &T);

    int M1, M2, D;
    for (int i = 0; i < T; i++) {
        scanf("%d %d %d", &M1, &M2, &D);

        int lessDay = D * M1 / (M1 + M2);
        
        printf("%d\n", D - lessDay);
    }
    
    return 0;
}
