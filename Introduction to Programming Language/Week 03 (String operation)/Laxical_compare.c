#include <stdio.h>
#include <string.h>
int main()
{
    char a[100], b[100];
    scanf("%s %s", a, b);

    // int i = 0;
    // while (1)
    // {
    //     if (a[i] == '\0' && b[i] == '\0')
    //     {
    //         printf("Same\n");
    //         break;
    //     }
    //     else if (a[i] == '\0')
    //     {
    //         printf("A smaller\n");
    //         break;
    //     }
    //     else if (b[i] == '\0')
    //     {
    //         printf("B smaller\n");
    //         break;
    //     }

    //     if (a[i] == b[i])
    //     {
    //         i++;
    //     }
    //     else if (a[i] < b[i])
    //     {
    //         printf("A smaller\n");
    //         break;
    //     }
    //     else
    //     {
    //         printf("B smaller\n");
    //         break;
    //     }
    // }

    int result = strcmp(a, b);
    if (result < 0)
    {
        printf("A smaller");
    }
    else if (result > 0)
    {
        printf("B smaller");
    }
    else
    {
        printf("Same");
    }
    return 0;
}