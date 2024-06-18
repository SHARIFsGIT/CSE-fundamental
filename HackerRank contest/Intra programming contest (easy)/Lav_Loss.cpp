#include <bits/stdc++.h>
using namespace std;

int main()
{
    int x, y, z;
    cin >> x >> y >> z;

    double loss = 1 - (y / 100.0);
    double original_price = x / loss;
    double profit = original_price * (z / 100.0);
    double new_price = original_price + profit;

    cout << fixed << setprecision(2) << new_price << endl;

    return 0;
}