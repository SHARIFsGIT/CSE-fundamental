#include <bits/stdc++.h>
using namespace std;

int main()
{
    string S;
    getline(cin, S);

    bool inside_word = false;
    int count = 0;
    for (char c : S)
    {
        if (isalpha(c) > 0)
        {
            if (inside_word == false)
            {
                count++;
            }
            inside_word = true;
        }
        else
        {
            inside_word = false;
        }
    }
    cout << count << endl;

    return 0;
}