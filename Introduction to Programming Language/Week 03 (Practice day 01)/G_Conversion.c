#include <stdio.h>
#include <string.h>

int main()
{
    char S[100001];
    gets(S);

    for (int i = 0; S[i] != '\0'; i++)
    {
        if (S[i] == ',')
            S[i] = ' ';
        else if (S[i] >= 'A' && S[i] <= 'Z')
            S[i] = S[i] + 32;
        else
            S[i] = S[i] - 32;
    }
    printf("%s", S);

    return 0;
}