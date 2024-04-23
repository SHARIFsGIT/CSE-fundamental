#include <stdio.h>
int main()
{
    char S[1001], rev[1001];
    scanf("%s", S);

    int len = strlen(S);

    for (int i = 0; i < len; i++)
    {
        if (S[i] != '\0')
        {
            rev[len - 1 - i] = S[i];
        }
    }

    int flag = 0;
    for (int i = 0; i < len; i++)
    {
        if (S[i] != rev[i])
        {
            flag = 1;
            break;
        }
    }

    if (flag == 0)
    {
        printf("YES\n");
    }
    else
    {
        printf("NO\n");
    }

    return 0;
}