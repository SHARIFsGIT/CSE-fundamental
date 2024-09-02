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

    void down_heapify(int index)
    {
        while (1)
        {
            int largest_index = index;

            int left_child = 2 * index + 1;
            int right_child = 2 * index + 2;

            if (left_child < nodes.size() && nodes[largest_index] < nodes[left_child])
            {
                largest_index = left_child;
            }

            if (right_child < nodes.size() && nodes[largest_index] < nodes[right_child])
            {
                largest_index = right_child;
            }

            if (index == largest_index)
            {
                break;
            }

            swap(nodes[largest_index], nodes[index]);

            index = largest_index;
        }
    }

    void push(int value)
    {
        nodes.push_back(value);
        up_heapify(nodes.size() - 1);
    }

    void pop(int index)
    {
        swap(nodes[index], nodes[nodes.size() - 1]);

        nodes.pop_back();

        down_heapify(index);
    }

    void buid_from_array(vector<int> &array)
    {
        nodes = array;

        int last_non_leaf_node = (array.size() / 2) - 1;

        for (int i = last_non_leaf_node; i >= 0; i--)
        {
            down_heapify(i);
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
};

int main()
{
    MaxHeap heap; // Obj of MaxHeap

    heap.push(1);
    heap.push(2);
    heap.push(3);
    heap.push(4);
    heap.push(5);

    heap.pop(0);

    vector<int> v = {2, 3, 4, 8, 11, 10, 9, 6};
    heap.buid_from_array(v);

    heap.print();

    return 0;
}