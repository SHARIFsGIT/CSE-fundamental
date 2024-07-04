#include <bits/stdc++.h>
using namespace std;

int main()
{
    list<int> mylist = {10, 20, 30, 40, 50};
    list<int> newlist;
    // newlist = mylist;
    newlist.assign(mylist.begin(), mylist.end());
    for (int value : newlist)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist2 = {10, 20, 30, 40, 50};
    mylist2.push_back(100);
    mylist2.push_front(200);
    mylist2.pop_back();
    mylist2.pop_front();
    for (int value : mylist2)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist3 = {10, 20, 30, 40, 50};
    mylist3.insert(next(mylist3.begin(), 2), 100);
    mylist3.insert(next(mylist3.begin(), 7), {500, 600});
    for (int value : mylist3)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist4 = {10, 20, 30, 40, 50};
    mylist4.erase(next(mylist4.begin(), 2));
    for (int value : mylist4)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist5 = {10, 20, 30, 40, 50};
    list<int> newlist2 = {1000, 2000, 3000};
    vector<int> v = {1, 2, 3};
    mylist5.insert(next(mylist5.begin(), 0), newlist2.begin(), newlist2.end());
    mylist5.insert(next(mylist5.begin(), 0), v.begin(), v.end());
    mylist5.erase(next(mylist5.begin(), 2), next(mylist5.begin(), 5));
    for (int value : mylist5)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist6 = {10, 20, 30, 40, 50, 30};
    replace(mylist6.begin(), mylist6.end(), 30, 100);
    for (int value : mylist6)
    {
        cout << value << " ";
    }
    cout << endl;

    list<int> mylist7 = {10, 20, 30, 40, 50, 30};
    auto it = find(mylist7.begin(), mylist7.end(), 30);
    if (it == mylist7.end())
    {
        cout << "Not found" << endl;
    }
    else
    {
        cout << "Found" << endl;
    }

    return 0;
}