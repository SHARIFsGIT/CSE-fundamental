#include <stdio.h>
int main()
{
    int test_case, width, height;
    scanf("%d", &test_case);

    for (int i = 0; i < test_case; i++)
    {
        scanf("%d %d", &width, &height);

        if (width == height)
        {
            printf("Square\n");
        }
        else
        {
            printf("Rectangle\n");
        }
    }

    return 0;
}