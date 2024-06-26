#include <bits/stdc++.h>
using namespace std;

void func(int * &p)
{
    // *p = 20;
    // p = NULL;
    cout << &p << endl;
}

int main()
{
    int value = 10;
    int *ptr = &value;

    func(ptr);

    cout << value << endl;
    cout << *ptr << endl;
    cout << &ptr << endl;

    return 0;
}