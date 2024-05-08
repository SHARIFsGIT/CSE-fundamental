#include <stdio.h>
int vowel(char S[], int i)
{
    if (S[i] == '\0')
    {
        return 0;
    }

    int ans = vowel(S, i + 1);

    if (S[i] >= 'A' && S[i] <= 'Z')
    {
        S[i] = S[i] + 32;
    }

    if (S[i] == 'a' || S[i] == 'e' || S[i] == 'i' || S[i] == 'o' || S[i] == 'u')
    {
        return ans + 1;
    }
    else
    {
        return ans;
    }
}
int main()
{
    char S[201];
    fgets(S, sizeof(S), stdin);

    int count = vowel(S, 0);
    printf("%d", count);
    return 0;
}