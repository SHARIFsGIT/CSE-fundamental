#include <stdio.h>

int main() {
    int x, y, T;
    scanf("%d %d %d", &x, &y, &T);

    for (int i = 0; i * x <= T; ++i) {
        int remaining_chocolates = T - (i * x);
        
        if (remaining_chocolates % y == 0) {
            printf("YES\n");
            return 0;
        }
    }
    printf("NO\n");
    return 0;
}
