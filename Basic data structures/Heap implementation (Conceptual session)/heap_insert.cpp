#include <bits/stdc++.h>
using namespace std;

class MaxHeap
{
public:
    vector<int> nodes;
    MaxHeap()
    {
        // constructor
    }

    void up_heapify(int index)
    {
        while (index > 0 && (nodes[index] > nodes[(index - 1) / 2]))
        {
            swap(nodes[index], nodes[(index - 1) / 2]);

            index = (index - 1) / 2;
        }
    }

    void print()
    {
        for (int node : nodes)
        {
            cout << node << " ";
        }
        cout << endl;
    }

    void push(int value)
    {
        nodes.push_back(value);
        up_heapify(nodes.size() - 1);
    }
};

int main()
{
    MaxHeap heap; // Obj of MaxHeap

    heap.push(1);
    heap.push(2);
    heap.push(3);
    heap.push(4);
    heap.push(5);

    heap.print();

    return 0;
}