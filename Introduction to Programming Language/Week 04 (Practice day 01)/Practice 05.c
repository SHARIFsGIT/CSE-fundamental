#include <stdio.h>
char capital_to_small(char X)
{
    return (X + 32);
}
int main()
{
    char X;
    scanf("%c", &X);
    char converted = capital_to_small(X);
    printf("%c", converted);
    return 0;
}