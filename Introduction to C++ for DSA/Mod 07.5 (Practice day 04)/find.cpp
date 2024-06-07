#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    getline(cin, str);

    string word;
    stringstream ss(str);

    int flag = 0;
    while (ss >> word)
    {
        if (word == "Sharif")
            flag = 1;
    }

    cout << (flag ? "Yes" : "No") << endl;

    return 0;
}