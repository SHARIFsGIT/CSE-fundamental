#include <bits/stdc++.h>
using namespace std;

int main()
{
    // For max heap:
    // priority_queue<int> pqueue;

    // For min heap:
    priority_queue<int, vector<int>, greater<int>> pqueue;

    while (true)
    {
        int command;
        cin >> command;

        if (command == 0)
        {
            int x;
            cin >> x;
            pqueue.push(x); // O(log N)
        }
        else if (command == 1)
        {
            pqueue.pop(); // O(log N)
        }
        else if (command == 2)
        {
            cout << pqueue.top() << endl; // O(1)
        }
        else
        {
            break;
        }
    }

    return 0;
}