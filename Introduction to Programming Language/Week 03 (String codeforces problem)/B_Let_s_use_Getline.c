#include <stdio.h>
int main()
{
    char S[1000001];
    fgets(S, sizeof(S), stdin);

    for (int i = 0; S[i] != '\\'; i++)
    {
        printf("%c", S[i]);
    }
    
    return 0;
}