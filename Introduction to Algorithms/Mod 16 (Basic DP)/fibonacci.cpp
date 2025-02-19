#include <bits/stdc++.h>
using namespace std;

// O(2^n) time | O(n) space
int fib(int n)
{
    if (n == 0 || n == 1)
    { 
        return n;
    }

    int fib1 = fib(n - 1);
    int fib2 = fib(n - 2);
    return fib1 + fib2;
}

int main()
{
    int n;
    cin >> n;

    cout << fib(n) << endl;

    return 0;
}