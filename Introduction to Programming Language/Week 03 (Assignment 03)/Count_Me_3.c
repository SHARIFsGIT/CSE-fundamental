#include <stdio.h>
int main()
{
    int T;
    scanf("%d", &T);

    char S[10001];
    for (int i = 0; i < T; i++)
    {
        scanf("%s\n", S);

        int capitals = 0, smalls = 0, digits = 0;
        for (int i = 0; S[i] != '\0'; i++)
        {
            if (S[i] >= 'A' && S[i] <= 'Z')
                capitals++;
            else if (S[i] >= 'a' && S[i] <= 'z')
                smalls++;
            else if (S[i] >= '0' && S[i] <= '9')
                digits++;
        }
        printf("%d %d %d\n", capitals, smalls, digits);
    }
    return 0;
}