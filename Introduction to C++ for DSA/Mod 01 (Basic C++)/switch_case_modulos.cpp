#include <iostream>
using namespace std;

int main()
{
    int x;
    cin >> x;
    switch (x % 2)
    {
    case 0:
        cout << "Even" << endl;
        break;

    default:
        cout << "Odd" << endl;
    }
    return 0;
}