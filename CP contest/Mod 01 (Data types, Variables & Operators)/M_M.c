#include <stdio.h>
int main()
{
    int n, m;
    scanf("%d %d", &n, &m);

    int x, y;
    scanf("%d %d", &x, &y);

    int bones = n * x;
    int blood = m * y;
    
    printf("%d", bones + blood);

    return 0;
}