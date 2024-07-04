#include <bits/stdc++.h>
using namespace std;

int main()
{
    list<int> mylist = {10, 50, 30, 60, 10};
    mylist.remove(10);
    for (int value : mylist)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist2 = {10, 50, 30, 60, 10};
    mylist2.sort();
    for (int value : mylist2)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist3 = {10, 50, 30, 60, 10};
    mylist3.sort(greater<int>());
    for (int value : mylist3)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist4 = {10, 50, 30, 60, 10};
    mylist4.sort(greater<int>());
    mylist4.unique();
    for (int value : mylist4)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist5 = {10, 50, 30, 60, 10, 10};
    mylist5.reverse();
    for (int value : mylist5)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist6 = {100, 50, 30, 60, 10, 32};
    cout << mylist6.front() << endl;
    cout << mylist6.back() << endl;
    cout << *next(mylist6.begin(), 3) << endl;

    return 0;
}