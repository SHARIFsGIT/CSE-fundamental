#include <bits/stdc++.h>
using namespace std;

int **func()
{
    int *a = new int;
    // cout << "Func: " << a << endl;
    *a = 10;
    // return a;
    cout << "Func: " << &a << endl;

    return &a;
}
int main()
{
    // int *a = new int;
    // *a = 10;
    // cout << a << endl;
    // cout << *a << endl;
    // delete a;

    int **p = func();
    cout << "Main: " << p << endl;

    return 0;
}