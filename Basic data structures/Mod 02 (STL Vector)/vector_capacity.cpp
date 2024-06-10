#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> v;
    cout << "Max size:" << v.max_size() << endl;

    cout << "Capacity:" << v.capacity() << endl;

    v.push_back(10);
    cout << "Capacity after 10 push back:" << v.capacity() << endl;
    v.push_back(20);
    cout << "Capacity after 20 push back:" << v.capacity() << endl;

    // Capacity doubled
    v.push_back(30);
    cout << "Capacity after 30 push back:" << v.capacity() << endl;
    v.push_back(40);
    cout << "Capacity after 40 push back:" << v.capacity() << endl;

    // Clear
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    v.push_back(40);
    v.push_back(50);
    cout << "Size after 10-50 push back:" << v.size() << endl;
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;

    v.clear();
    cout << "New size after clear:" << v.size() << endl;
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << "Value available after clear:" << v[0] << endl;
    cout << "Value available after clear:" << v[1] << endl;
    cout << endl;

    // Resize:
    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    v.push_back(40);
    v.push_back(50);
    v.resize(3);
    cout << "Size after resize 10-50 push back:" << v.size() << endl;
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
    v.resize(7, 100);
    cout << "Size after resize 10-50 push back:" << v.size() << endl;
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << " ";
    }

    return 0;
}