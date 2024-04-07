#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char X;
    scanf("%c", &X);
    if (X >= 'A' && X <= 'Z')
    {
        printf("%c", X+32);
    }
    else
    {
        printf("%c", X-32);
    }

    return 0;
}


/*
int main()
{
    char X;
    scanf("%c", &X);
    if (X >= 97 && X <= 122)
    {
        int result = X -32;
        printf("%c", result);
    }
    else
    {
        int result = X + 32;
        printf("%c", result);
    }
    return 0;
}
*/
