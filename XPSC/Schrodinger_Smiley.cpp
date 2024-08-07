#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        string s;
        cin >> s;

        int found = 0;

        for (int j = 0; j < n; j++)
        {
            if (s[j] == ':')
            {
                int close = 0;
                for (int k = j + 1; k < n; k++)
                {
                    if (s[k] == ')')
                    {
                        close++;
                    }
                    else if (s[k] == ':')
                    {
                        if (close > 0)
                        {
                            found++;
                        }
                        break;
                    }
                    else if (s[k] == '(')
                    {
                        break;
                    }
                }
            }
        }

        cout << found << endl;
    }

    return 0;
}
