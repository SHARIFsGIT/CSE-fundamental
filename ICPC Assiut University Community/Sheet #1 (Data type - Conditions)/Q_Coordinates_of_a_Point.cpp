#include <bits/stdc++.h>
using namespace std;

int main() {
    float x, y;
    cin >> x >> y;

    string result = (x == 0.0 && y == 0.0) ? "Origem" :
                    (x == 0.0) ? "Eixo Y" :
                    (y == 0.0) ? "Eixo X" :
                    (x > 0.0 && y > 0.0) ? "Q1" :
                    (x < 0.0 && y > 0.0) ? "Q2" :
                    (x < 0.0 && y < 0.0) ? "Q3" : "Q4";

    cout << result << endl;

    return 0;
}