#include <bits/stdc++.h>
using namespace std;

int main()
{
    string line;
    while (getline(cin, line))
    {
        string result;
        for (char c = 'a'; c <= 'z'; ++c)
        {
            for (char ch : line)
            {
                if (ch == c)
                {
                    result += ch;
                }
            }
        }
        cout << result << endl;
    }
    return 0;
}