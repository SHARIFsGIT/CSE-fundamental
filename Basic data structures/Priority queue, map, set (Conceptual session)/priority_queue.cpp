#include <bits/stdc++.h>
using namespace std;

int main()
{
    priority_queue<int> pq;

    pq.push(10);
    pq.push(40);
    pq.push(30);

    while (!pq.empty())
    {
        cout << pq.top() << endl;
        pq.pop();
    }

    priority_queue<int, vector<int>, greater<int>> min_heap;

    min_heap.push(10);
    min_heap.push(40);
    min_heap.push(30);

    while (!min_heap.empty())
    {
        cout << min_heap.top() << endl;
        min_heap.pop();
    }

    return 0;
}