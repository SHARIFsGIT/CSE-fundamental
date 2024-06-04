#include <bits/stdc++.h>
using namespace std;
int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        string X;
        cin >> X;

        string Y;
        cin >> Y;
        while (X.find(Y) != -1)
        {
            X.replace(X.find(Y), Y.size(), "#");
        }
        cout << X << endl;
    }

    return 0;
}