#include <stdio.h>
#include <string.h>
int main()
{
    char S[100];
    scanf("%s", S);

    int count[26] = {0};
    for (int i = 0; i < strlen(S); i++)
    {
        int value = S[i] - 'a';
        count[value]++;
    }

    // for (int i = 0; i < 26; i++)
    // {
    //     if (count[i] != 0)
    //     {
    //         printf("%c - %d\n", i + 'a', count[i]);
    //     }
    // }

    for (int i = 0; i < strlen(S); i++)
    {
        int value = S[i] - 'a';
        // printf("%c - %d\n", value + 'a', count[value]);
        if (count[value] != 0)
        {
            printf("%c - %d\n", value + 'a', count[value]);
        }

        count[value] = 0;
    }

    return 0;
}