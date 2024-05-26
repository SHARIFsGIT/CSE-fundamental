#include <bits/stdc++.h>
using namespace std;

int main()
{
    char S;
    int A, B;

    cin >> A >> S >> B;

    ((S == '>' && A > B) || (S == '<' && A < B) || (S == '=' && A == B)) ? cout << "Right" : cout << "Wrong";

    return 0;
}