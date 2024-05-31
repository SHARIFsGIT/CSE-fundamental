#include <bits/stdc++.h>
using namespace std;

namespace Sharif
{
    int age1 = 29;

    void hello1()
    {
        cout << "Hello from Sharif" << endl;
    }
}
namespace Islam
{
    int age2 = 25;

    void hello2()
    {
        cout << "Hello from Islam" << endl;
    }
}

using namespace Sharif;
using namespace Islam;
int main()
{
    // cout << Sharif::age1 << endl;
    // cout << Islam::age2 << endl;
    cout << age1 << endl;
    hello1();
    cout << age2 << endl;
    Islam::hello2();

    return 0;
}