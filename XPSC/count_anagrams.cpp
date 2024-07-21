#include <bits/stdc++.h>
using namespace std;

int main()
{
    string text, pattern;
    cin >> text >> pattern;

    int k = pattern.size();
    int i = 0, j = 0;

    int freq1[26] = {0};
    int freq2[26] = {0};

    for (char c : pattern)
    {
        freq1[c - 'a']++;
    }

    int ans = 0;
    while (j < text.size())
    {
        freq2[text[j] - 'a']++;
        if (j < k - 1)
        {
            j++;
        }
        else
        {
            bool flag = true;
            for (int index = 0; index < 26; index++)
            {
                if (freq1[index] != freq2[index])
                {
                    flag = false;
                    break;
                }
            }
            if (flag)
            {
                ans++;
            }
            freq2[text[i] - 'a']--;
            i++;
            j++;
        }
    }
    cout << ans << endl;

    return 0;
}