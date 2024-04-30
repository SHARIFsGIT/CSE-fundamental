#include <stdio.h>
char small_to_capital(char X)
{
    return (X - 32);
}
int main()
{
    char X;
    scanf("%c", &X);
    char converted = small_to_capital(X);
    printf("%c", converted);
    return 0;
}