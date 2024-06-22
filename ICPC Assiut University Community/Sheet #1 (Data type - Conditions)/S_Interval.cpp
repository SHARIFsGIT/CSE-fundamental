#include <bits/stdc++.h>
using namespace std;

int main()
{
    float x;
    cin >> x;

    cout << ((x >= 0 && x <= 25) ? "Interval [0,25]" :
            (x > 25 && x <= 50) ? "Interval (25,50]" : 
            (x > 50 && x <= 75) ? "Interval (50,75]" : 
            (x > 75 && x <= 100) ? "Interval (75,100]" : "Out of Intervals") << endl;

    return 0;
}