#include <bits/stdc++.h>
using namespace std;

int main()
{
    list<int> myList1;
    cout << myList1.size() << endl;

    list<int> myList2(10);
    cout << myList2.size() << endl;

    list<int> myList3(10);
    cout << myList3.front() << endl;

    list<int> myList4(10, 5);
    cout << myList4.front() << endl;

    for (auto it = myList4.begin(); it != myList4.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;

    list<int> myList5 = {1, 2, 3, 4, 5};
    list<int> myList6(myList5);

    for (auto it = myList6.begin(); it != myList6.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;

    int array[5] = {10, 20, 30, 40, 50};
    list<int> myList7(array, array + 5);

    for (auto it = myList7.begin(); it != myList7.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;

    vector<int> v = {100, 200, 300, 400, 500};
    list<int> myList8(v.begin(), v.end());

    // for (auto it = myList8.begin(); it != myList8.end(); it++)
    // {
    //     cout << *it << " ";
    // }
    for (int value : myList8)
    {
        cout << value << " ";
    }

    return 0;
}