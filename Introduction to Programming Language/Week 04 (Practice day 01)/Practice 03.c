#include <stdio.h>
int char_to_ascii(char X)
{
    return X;
}
int main()
{
    char X;
    scanf("%c", &X);
    int converted = char_to_ascii(X);
    printf("%d", converted);
    return 0;
}