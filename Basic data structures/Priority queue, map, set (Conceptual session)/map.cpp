#include <bits/stdc++.h>
using namespace std;

int main()
{
    map<string, int> identity;

    // Method 01:
    identity["Tamim"] = 18;
    identity["Shanto"] = 23;

    cout << identity["Tamim"] << endl;

    // Method 02:
    identity.insert(make_pair("Sayumo", 25));
    cout << identity["Sayumo"] << endl;

    // Method 03:
    identity.insert({"Sakib", 30});
    cout << identity["Sakib"] << endl;

    for (auto pair : identity)
    {
        cout << pair.first << " " << pair.second << endl;
    }

    return 0;
}