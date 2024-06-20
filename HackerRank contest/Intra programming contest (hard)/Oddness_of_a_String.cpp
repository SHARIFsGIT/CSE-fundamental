#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, q;
        cin >> n >> q;

        string str;
        cin >> str;

        for (int i = 0; i < q; i++)
        {
            int l, r;
            cin >> l >> r;
            l--;

            int freq_array[26] = {0};
            for (int i = l; i < r; i++)
            {
                freq_array[str[i] - 'a']++;
            }

            int odd = 0;
            for (int i = 0; i < 26; i++)
            {
                if (freq_array[i] % 2 != 0)
                {
                    odd++;
                }
            }
            cout << odd << endl;
        }
    }

    return 0;
}