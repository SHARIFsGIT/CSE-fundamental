#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v = {10, 20, 30, 40, 50};
    v.erase(v.begin() + 1, v.begin() + 3);
    // v.erase(v.begin() + 1, v.end() - 2);
    for (int value : v)
    {
        cout << value << " ";
    }

    return 0;
}