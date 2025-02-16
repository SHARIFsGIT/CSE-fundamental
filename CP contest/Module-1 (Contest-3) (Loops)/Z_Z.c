#include <stdio.h>

int findMaxNumber(int n1, int n2, int n3)
{
    int temp;
    for (int i = 0; i < 2; i++)
    {
        if (n1 < n2)
        {
            temp = n1;
            n1 = n2;
            n2 = temp;
        }
        if (n2 < n3)
        {
            temp = n2;
            n2 = n3;
            n3 = temp;
        }
    }
    return n1 * 100 + n2 * 10 + n3;
}

int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int a1, a2, a3, b1, b2, b3;
        scanf("%d %d %d %d %d %d", &a1, &a2, &a3, &b1, &b2, &b3);

        int aliceScore = findMaxNumber(a1, a2, a3);
        int bobScore = findMaxNumber(b1, b2, b3);

        if (aliceScore > bobScore)
        {
            printf("Alice\n");
        }
        else if (bobScore > aliceScore)
        {
            printf("Bob\n");
        }
        else
        {
            printf("Tie\n");
        }
    }
    return 0;
}