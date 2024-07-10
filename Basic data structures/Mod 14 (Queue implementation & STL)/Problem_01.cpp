#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m, num;
    cin >> n;

    queue<int> q1;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        q1.push(num);
    }

    cin >> m;

    queue<int> q2;
    for (int i = 0; i < m; i++)
    {
        cin >> num;
        q2.push(num);
    }

    queue<int> mergedQueue;
    while (!q1.empty())
    {
        mergedQueue.push(q1.front());
        q1.pop();
    }
    while (!q2.empty())
    {
        mergedQueue.push(q2.front());
        q2.pop();
    }

    while (!mergedQueue.empty())
    {
        cout << mergedQueue.front() << " ";
        mergedQueue.pop();
    }

    return 0;
}