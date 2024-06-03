#include <bits/stdc++.h>
using namespace std;

int main()
{
    int size = 100000 + 5;
    char str[size];

    while (cin.getline(str, size))
    {
        int len = strlen(str);

        sort(str, str + len);

        for (int i = 0; i < len; i++)
        {
            if (str[i] != ' ')
            {
                cout << str[i];
            }
        }
        cout << endl;
    }

    return 0;
}