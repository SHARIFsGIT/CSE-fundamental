#include <iostream>
using namespace std;

int main()
{
    int a;
    long long int b;
    cin >> a >> b;
    cout << a << " " << b << endl;

    char c;
    cin >> c;
    cout << c << endl;
    cout << int(c) << endl;

    int ascii = c;
    cout << ascii << endl;

    int d = 10;
    long long int e = (long long int)(d);
    cout << d << endl;
    cout << e << endl;

    int f;
    char g;
    cin >> f >> g;
    cout << f << " " << g << endl;

    return 0;
}