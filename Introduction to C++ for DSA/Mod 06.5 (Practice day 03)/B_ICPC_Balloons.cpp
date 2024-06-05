#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int string_size;
        cin >> string_size;

        string str;
        cin >> str;

        int freq[26] = {0};
        for (char character : str)
        {
            freq[character - 'A']++;
        }

        int count = 0;
        for (int i = 0; i < 26; i++)
        {
            if (freq[i] != 0)
            {
                if (freq[i] == 1)
                {
                    count += 2;
                }
                else
                {
                    count += freq[i] + 1;
                }
            }
        }
        cout << count << endl;
    }

    return 0;
}