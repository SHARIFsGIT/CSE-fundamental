#include <bits/stdc++.h>
using namespace std;

class comparator
{
public:
    bool operator()(pair<int, int> &a, pair<int, int> &b)
    {
        if (a.second < b.second)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};

int main()
{
    priority_queue<pair<int, int>, vector<pair<int, int>>, comparator> pq;

    pq.push({1, 3});
    pq.push({2, 1});
    pq.push({4, 0});

    while (!pq.empty())
    {
        cout << pq.top().first << " " << pq.top().second << endl;
        pq.pop();
    }

    return 0;
}