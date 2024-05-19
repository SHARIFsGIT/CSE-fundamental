#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a, b;
    cin >> a >> b;

    int minimum = min(a, b);
    int maximum = max(a, b);
    cout << "Minimum: " << minimum << " " << "Maximum: " << maximum << endl;

    int c, d;
    cin >> a >> b >> c >> d;
    int minimum_multple = min({a, b, c, d});
    int maximum_multple = max({a, b, c, d});
    cout << "Minimum: " << minimum_multple << " " << "Maximum: " << maximum_multple << endl;

    return 0;
}