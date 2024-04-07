#include <stdio.h>

int main() {
    int n, m;

    scanf("%d %d", &n, &m);

    int gifts_per_child = n / m;
    int remaining_gifts = n % m;

    printf("%d %d", gifts_per_child, remaining_gifts);

    return 0;
}

