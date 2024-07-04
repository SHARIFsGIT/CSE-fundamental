#include <bits/stdc++.h>
using namespace std;

int main()
{
    list<int> mylist = {10, 20, 30};
    cout << mylist.max_size() << endl;

    for (int value : mylist)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist2 = {10, 20, 30};
    cout << mylist2.max_size() << endl;
    mylist2.clear();
    cout << mylist2.size() << endl;

    for (int value : mylist2)
    {
        cout << "Value: " << value << " ";
    }

    list<int> mylist3 = {10, 20, 30};
    mylist3.resize(2);
    cout << mylist3.size() << endl;

    for (int value : mylist3)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist4 = {10, 20, 30};
    mylist4.resize(2);
    mylist4.resize(5, 100);
    cout << mylist4.size() << endl;

    for (int value : mylist4)
    {
        cout << value << " ";
    }
    cout << endl;

    return 0;
}