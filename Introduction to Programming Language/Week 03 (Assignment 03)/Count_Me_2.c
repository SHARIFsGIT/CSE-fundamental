#include <stdio.h>
int main()
{
    char S[100001];
    scanf("%s", S);

    int cons = 0;
    for (int i = 0; S[i] != '\0'; i++)
    {
        if (S[i] != 'a' && S[i] != 'e' && S[i] != 'i' && S[i] != 'o' && S[i] != 'u')
        {
            cons++;
        }
    }
    printf("%d", cons);

    return 0;
}