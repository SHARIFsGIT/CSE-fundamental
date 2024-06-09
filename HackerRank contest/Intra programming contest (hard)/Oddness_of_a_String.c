#include <stdio.h>
#include <string.h>

int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n, q;
        scanf("%d %d", &n, &q);
        
        char s[1000001];
        scanf("%s", s);

        while (q--)
        {
            int l, r;
            scanf("%d %d", &l, &r);
            l--;

            int charCount[26] = {0};
            for (int i = l; i < r; i++)
            {
                charCount[s[i] - 'a']++;
            }

            int oddness = 0;
            for (int i = 0; i < 26; i++)
            {
                if (charCount[i] % 2 != 0)
                {
                    oddness++;
                }
            }
            printf("%d\n", oddness);
        }
    }

    return 0;
}
