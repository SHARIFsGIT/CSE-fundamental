#include <iostream>
using namespace std;

int main()
{
    int x = 100;
    if (x == 10)
    {
        cout << "X is 10" << endl;
    }
    else
    {
        cout << "X is not 10" << endl;
    }

    (x == 100) ? cout << "X is 100" << endl : cout << "X is not 100" << endl;

    return 0;
}