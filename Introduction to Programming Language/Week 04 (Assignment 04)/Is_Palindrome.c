#include <stdio.h>
#include <string.h>

int is_palindrome(char *string, char *reverse)
{
    int len = strlen(string);
    for (int i = len - 1; i >= 0; i--)
    {
        reverse[len - 1 - i] = string[i];
    }
    for (int i = 0; i < len; i++)
    {
        if (string[i] != reverse[i])
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    char S[1001];
    char R[1001];
    scanf("%s", S);

    int result = is_palindrome(S, R);

    if (result == 0)
        printf("Not Palindrome\n");
    else
        printf("Palindrome\n");
    return 0;
}
