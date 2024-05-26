#include <bits/stdc++.h>
using namespace std;

int main()
{
    int A, B, C;
    char S, Q;

    cin >> A >> S >> B >> Q >> C;

    int result = (S == '+') ? (A + B) : (S == '-') ? (A - B)
                                                   : (A * B);

    (result == C) ? cout << "Yes" : cout << result << endl;

    return 0;
}