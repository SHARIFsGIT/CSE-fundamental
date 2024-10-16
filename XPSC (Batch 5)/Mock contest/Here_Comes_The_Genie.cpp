#include <bits/stdc++.h>
using namespace std;

void collectMaximumBalls()
{
    int n;
    long long totalBalls = 0;
    unordered_set<int> collectedBalls;
    cin >> n;
    vector<int> balls(n);

    for (auto &ball : balls)
    {
        cin >> ball;
    }

    sort(balls.begin(), balls.end(), greater<int>());

    int maxBalls = balls[0];

    for (int i = 0; i < n; i++)
    {
        maxBalls = min(maxBalls, balls[i]);

        while (maxBalls && collectedBalls.count(maxBalls))
        {
            maxBalls--;
        }
        
        if (maxBalls > 0)
        {
            totalBalls += maxBalls;
            collectedBalls.insert(maxBalls);
        }
    }

    cout << totalBalls << endl;
}

int main()
{
    collectMaximumBalls();
    return 0;
}
