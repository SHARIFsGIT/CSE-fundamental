#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        cin >> n;

        vector<int> array(n);
        for (int i = 0; i < n; i++)
        {
            cin >> array[i];
        }

        vector<int> copy_of_array = array;

        sort(copy_of_array.begin(), copy_of_array.end());

        cout << ((array == copy_of_array) ? "YES" : "NO") << endl;
    }

    return 0;
}