#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, num, d;
    cin >> n;

    queue<int> q;
    for (int i = 0; i < n; i++)
    {
        cin >> num;
        q.push(num);
    }

    cin >> d;
    queue<int> copyQ;
    int size = q.size();
    for (int i = 1; i <= size; i++)
    {
        int current = q.front();
        q.pop();
        if (i != d)
        {
            copyQ.push(current);
        }
    }

    while (!copyQ.empty())
    {
        cout << copyQ.front() << " ";
        copyQ.pop();
    }

    return 0;
}