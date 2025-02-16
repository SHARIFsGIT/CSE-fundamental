#include <stdio.h>
int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int k;
        scanf("%d", &k);

        int serial_no = 1;
        for (int i = 1;; i++)
        {
            if (i % 3 == 0 || i % 10 == 3)
            {
                continue;
            }

            if (serial_no == k)
            {
                printf("%d\n", i);
                break;
            }
            serial_no++;
        }
    }

    return 0;
}