#include <stdio.h>
int main()
{
    int a, b, x, y;
    scanf("%d %d %d %d", &a, &b, &x, &y);

    int messi = 2 * a + b;
    int ronaldo = 2 * x + y;

    if (messi > ronaldo)
    {
        printf("Messi\n");
    }
    else if (messi < ronaldo)
    {
        printf("Ronaldo\n");
    }
    else
    {
        printf("Equal\n");
    }

    return 0;
}