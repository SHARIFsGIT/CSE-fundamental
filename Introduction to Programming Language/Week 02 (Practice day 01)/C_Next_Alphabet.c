#include <stdio.h>
int main()
{
    char C;
    scanf("%c", &C);

    if (C >= 'a' && C <= 'y')
    {
        printf("%c", C+1);
    }
    if (C == 'z')
    {
        printf("%c", C-25);
    }
    
    return 0;
}