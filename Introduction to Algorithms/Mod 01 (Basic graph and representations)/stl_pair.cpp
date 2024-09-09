#include <bits/stdc++.h>
using namespace std;

// class Pair
// {
// public:
//     int first;
//     int second;

//     void make_pair(int a, int b)
//     {
//         first = a;
//         second = b;
//     }
// };

int main()
{
    pair<int, int> p;
    p = make_pair(1, 2);
    // Pair p;
    // p.make_pair(1, 2);

    cout << p.first << " " << p.second;

    return 0;
}