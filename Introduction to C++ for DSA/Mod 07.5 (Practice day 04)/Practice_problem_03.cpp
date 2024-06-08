#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    getline(cin, str);

    string word;
    stringstream ss(str);

    int count = 0;
    while (ss >> word)
    {
        if (word == "john")
        {
            count++;
        }
    }
    cout << count << endl;

    return 0;
}