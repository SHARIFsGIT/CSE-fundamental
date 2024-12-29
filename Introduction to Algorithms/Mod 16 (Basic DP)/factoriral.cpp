#include <bits/stdc++.h>
using namespace std;

// O(n) time | O(n) space
int fact(int n)
{
    if (n == 0)
    {
        return 1;
    }

    int smallFact = fact(n - 1);
    return n * smallFact;
}

int main()
{
    int n;
    cin >> n;

    cout << fact(n) << endl;

    /* 
    // O(n) time | O(1) space
    int fact = 1;
    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }
    cout << fact << endl; 
    */

    return 0;
}