#include <bits/stdc++.h>
using namespace std;

int main()
{
    string sentence;
    getline(cin, sentence);

    string word;
    stringstream ss(sentence);

    map<string, int> m;

    while (ss >> word)
    {
        // cout << word << endl;
        m[word]++;
    }

    // for (auto it = m.begin(); it != m.end(); it++)
    // {
    //     cout << it->first << " " << it->second << endl;
    // }

    cout << m["love"] << endl;

    return 0;
}