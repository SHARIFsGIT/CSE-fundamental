#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char X;
    scanf("%c", &X);
    if (X >= 'A' && X <= 'z')
    {
        printf("ALPHA\n");

        if (X >= 'A' && X <= 'Z')
        {
            printf("IS CAPITAL");
        }
        else
        {
            printf("IS SMALL");
        }
    }
    else
    {
        printf("IS DIGIT");
    }

    return 0;
}

