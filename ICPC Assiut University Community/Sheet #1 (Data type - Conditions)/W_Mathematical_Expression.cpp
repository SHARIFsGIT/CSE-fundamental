#include <bits/stdc++.h>
using namespace std;

int main()
{
    int A, B, C;
    char S, Q;

    cin >> A >> S >> B >> Q >> C;

    int result;
    switch (S)
    {
    case '+':
        result = A + B;
        break;

    case '-':
        result = A - B;
        break;

    case '*':
        result = A * B;
        break;
    }

    (result == C) ? cout << "Yes" << endl : cout << result << endl;

    return 0;
}