#include <bits/stdc++.h>
using namespace std;

class Solution
{
public:
    int longestKSubstr(string s, int k)
    {
        int i = 0, j = 0, n = s.size(), ans = -1, unique = 0;
        int freq[26] = {0};

        while (j < n)
        {
            char c = s[j];
            if (freq[c - 'a'] == 0)
            {
                unique++;
            }
            freq[c - 'a']++;

            while (unique > k)
            {
                char leftC = s[i];
                freq[leftC - 'a']--;
                if (freq[leftC - 'a'] == 0)
                {
                    unique--;
                }
                i++;
            }

            if (unique == k)
            {
                ans = max(ans, j - i + 1);
            }

            j++;
        }

        return ans;
    }
};

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;
        Solution ob;
        cout << ob.longestKSubstr(s, k) << endl;
    }
    return 0;
}
