#include <bits/stdc++.h>
using namespace std;

int main()
{
    char str[100005];

    while (cin.getline(str, 100005))
    {
        sort(str, str + strlen(str));

        for (int i = 0; i < strlen(str); i++)
        {
            if (str[i] == ' ')
            {
                continue;
            }
            else
            {
                cout << str[i];
            }
        }
        cout << endl;
    }

    return 0;
}