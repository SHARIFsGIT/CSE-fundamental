#include <bits/stdc++.h>
using namespace std;

int main()
{
    map<string, int> m;

    // O(log n):
    m.insert({"Sharif", 75});
    m.insert({"Arif", 55});
    m.insert({"Naif", 88});
    m.insert({"Tarif", 95});
    m["Yafan"] = 99;

    // O(log n):
    // for (auto it = m.begin(); it != m.end(); it++)
    // {
    //     cout << it->first << " " << it->second << endl;
    // }

    cout << m["Sharif"] << endl;
    cout << m["sharif"] << endl;

    if (m.count("shrif"))
    {
        cout << "Found" << endl;
    }
    else
    {
        cout << "Not Found" << endl;
    }

    return 0;
}