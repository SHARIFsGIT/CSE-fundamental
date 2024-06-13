#include <bits/stdc++.h>
using namespace std;

int main()
{
    // 01: Initialize a Vector
    vector<int> v;
    for (int i = 0; i < 10; i++)
    {
        v.push_back(i + 1);
    }

    // 02: Print Initial Vector Properties
    cout << "Size: " << v.size() << endl;
    cout << "Capacity: " << v.capacity() << endl;
    cout << "Max Size: " << v.max_size() << endl;

    // 03: Resize the Vector
    v.resize(20, 0);
    cout << "Size after resize: " << v.size() << endl;
    cout << "Capacity after resize: " << v.capacity() << endl;

    // 04: Clear the Vector
    v.clear();
    cout << "Size after clear: " << v.size() << endl;
    cout << "Capacity after clear: " << v.capacity() << endl;

    // 05: Check if the Vector is Empty
    cout << "Is the vector empty? " << (v.empty() ? "Yes" : "No") << endl;

    // 06: Resize to Original Size
    v.resize(10, 100);
    cout << "Resized to original size: " << v.size() << endl;
    cout << "Resized to original capacity: " << v.capacity() << endl;
    for (int element : v)
    {
        cout << element << " ";
    }

    return 0;
}