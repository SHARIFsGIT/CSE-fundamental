#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n, k;
        scanf("%d %d", &n, &k);

        int perPersonBill = n / (k + 1);

        int totalFromFriend = perPersonBill * k;

        printf("%d\n", n - totalFromFriend);
    }

    return 0;
}