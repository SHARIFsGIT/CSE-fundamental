#include <bits/stdc++.h>
using namespace std;

void palindrome()
{
    string str;
    cin >> str;

    map<char, int> counts;

    int n = str.size();

    for (int i = 0; i < n; i++)
    {
        counts[str[i]]++;
    }

    /*
        for (auto it : counts)
        {
            cout << it.first << " " << it.second << "\n";
        }
     */

    int oddCount = 0;

    for (auto it : counts)
    {
        char character = it.first;
        int occured = it.second;

        if (occured % 2 != 0)
        {
            oddCount++;
        }
    }

    if (oddCount > 1)
    {
        cout << "NO SOLUTION" << endl;
        return;
    }

    string first, middle, last;

    for (auto it : counts)
    {
        char character = it.first;
        int occured = it.second;

        if (occured % 2 != 0)
        {
            for (int i = 1; i <= occured; i++)
            {
                middle.push_back(character);
            }
        }
        else
        {
            for (int i = 1; i <= (occured / 2); i++)
            {
                first.push_back(character);
                last.push_back(character);
            }
        }
    }

    reverse(last.begin(), last.end());

    cout << first + middle + last << endl;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    palindrome();

    return 0;
}