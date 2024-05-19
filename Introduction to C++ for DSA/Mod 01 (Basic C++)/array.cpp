#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int array[n];
    // for (int i = 0; i < 5; i++)
    // {
    //     cout << "Hello " << i << "!" << endl;
    // }

    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    for (int i = 0; i < n; i++)
    {
        cout << array[i] << endl;
    }

    return 0;
}