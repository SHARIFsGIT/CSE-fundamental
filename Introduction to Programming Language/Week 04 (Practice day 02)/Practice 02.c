#include <stdio.h>
int my_len(char *string)
{
    int count = 0;
    for (int i = 0; string[i] != '\0'; i++)
    {
        count++;
    }
    return count;
}
int main()
{
    char string[1001];
    scanf("%s", string);

    int result = my_len(string);
    printf("%d", result);
    return 0;
}