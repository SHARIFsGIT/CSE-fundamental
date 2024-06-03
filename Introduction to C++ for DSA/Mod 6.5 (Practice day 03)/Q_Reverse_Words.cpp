#include <bits/stdc++.h>
using namespace std;

int main()
{
    string S;
    // getline takes the leading or heading spaces
    getline(cin, S);

    stringstream ss(S);

    string word;
    ss >> word;
    reverse(word.begin(), word.end());
    cout << word;

    for (; ss >> word;)
    {
        reverse(word.begin(), word.end());
        cout << " " << word;
    }

    return 0;
}