#include <stdio.h>
#include <math.h>
int main()
{
    int N;
    scanf("%d", &N);

    int reduce = floor(N / 2);
    int control = 6 + reduce;
    int star = 1;
    int space = control - 1;

    for (int i = 1; i <= control; i++)
    {
        for (int j = 1; j <= space; j++)
        {
            printf(" ");
        }
        for (int j = 1; j <= star; j++)
        {
            printf("*");
        }
        space--;
        star = star + 2;
        printf("\n");
    }

    int lower_space = 5;
    for (int i = 1; i <= lower_space; i++)
    {
        for (int j = 1; j <= 5; j++)
        {
            printf(" ");
        }
        for (int k = 1; k <= N; k++)
        {
            printf("*");
        }
        printf("\n");
    }

    return 0;
}


// #include <stdio.h>
// #include <limits.h>
// int main()
// {
//     int n;
//     scanf("%d", &n);
//     int sample_n = 1;
//     int res = 6, l = 5, s = 5, k = 1;
//     int difference = abs(n - sample_n) / 2;
//     int line = res + difference;
//     int space = line - 1;
//     for (int i = 1; i <= line; i++)
//     {
//         for (int j = 1; j <= space; j++)
//         {
//             printf(" ");
//         }
//         for (int j = 1; j <= k; j++)
//         {
//             printf("*");
//         }
//         printf("\n");
//         space--;
//         k += 2;
//     }
//     for (int i = 1; i <= l; i++)
//     {
//         for (int j = 1; j <= s; j++)
//         {
//             printf(" ");
//         }
//         for (int j = 1; j <= n; j++)
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
//     return 0;
// }


// #include <stdio.h>
// int main()
// {
//     int n;
//     scanf("%d", &n);
//     int s = (6 + (n - 1) / 2) - 1, k = 1, p = n;

//     for (int i = 0; i < 6 + (n - 1) / 2; i++)
//     {
//         for (int j = 0; j < s; j++)
//         {
//             printf(" ");
//         }
//         for (int j = 0; j < k; j++)
//         {
//             printf("*");
//         }
//         if (i < 6 + (n - 1) / 2)
//         {
//             s--;
//             k = k + 2;
//         }
//         printf("\n");
//     }

//     for (int i = 0; i < 5; i++)
//     {
//         for (int j = 0; j < 5; j++)
//         {
//             printf(" ");
//         }
//         for (int j = 0; j < p; j++)
//         {
//             printf("*");
//         }
//         printf("\n");
//     }
//     return 0;
// }