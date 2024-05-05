#include <stdio.h>
void func(int i)
{
    if (i == 6)
    {
        return;
    }

    func(i + 1);
    printf("%d\n", i);
}
int main()
{
    func(1);
    return 0;
}