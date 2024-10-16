#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, target;
    cin >> n;

    vector<int> books(n);

    for (int i = 0; i < n; i++)
    {
        cin >> books[i];
    }

    cin >> target;

    int result = -1;
    
    for (int i = 0; i < n; i++)
    {
        result = (books[i] == target) ? i : result;
    }

    cout << result << endl;

    return 0;
}
