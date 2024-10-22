#include <bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
int parentArray[N];

void dsu_initialize(int n)
{
    for (int i = 0; i < n; i++)
    {
        parentArray[i] = -1;
    }

    parentArray[1] = 3;
    parentArray[2] = 1;
}

// int find(int node)
// {
//     if (parentArray[node] == -1)
//     {
//         return node;
//     }
//     return parentArray[node] = find(parentArray[node]);
// }

int dsu_find(int node)
{
    if (parentArray[node] == -1)
    {
        return node;
    }

    int leder = dsu_find(parentArray[node]);
    parentArray[node] = leder;
    return leder;
}

int main()
{
    dsu_initialize(4);
    cout << dsu_find(0) << endl;
    cout << dsu_find(1) << endl;
    cout << dsu_find(2) << endl;
    cout << dsu_find(3) << endl;
    return 0;
}