#include <bits/stdc++.h>
using namespace std;

bool isSubsequence(string word1, string word2)
{
    int position = 0;

    for (char c : word1)
    {
        if (c == word2[position])
        {
            position++;
        }

        if (position == word2.length())
        {
            return true;
        }
    }
    return position == word2.length();
}

int main()
{
    string word1, word2;

    while (cin >> word1 >> word2)
    {
        cout << (isSubsequence(word1, word2) ? "Possible" : "Impossible") << endl;
    }

    return 0;
}
