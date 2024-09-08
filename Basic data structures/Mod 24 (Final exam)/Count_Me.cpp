#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    cin.ignore();

    while (t--)
    {
        string s;
        getline(cin, s);

        map<string, int> m;

        string word;
        stringstream ss(s);
        string frq_word;

        int count = 0;
        while (ss >> word)
        {
            m[word]++;

            if (m[word] > count)
            {
                count = m[word];
                frq_word = word;
            }
        }
        cout << frq_word << " " << count << endl;
    }

    return 0;
}