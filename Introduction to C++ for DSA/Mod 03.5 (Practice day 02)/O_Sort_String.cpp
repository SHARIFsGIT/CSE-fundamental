#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;

    string S;
    cin >> S;

    int freq[26] = {0};
    for (int i = 0; i < N; i++)
    {
        freq[S[i] - 'a']++;
    }

    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < freq[i]; j++)
        {
            cout << (char)(i + 'a');
        }
    }
    cout << endl;
    return 0;
}