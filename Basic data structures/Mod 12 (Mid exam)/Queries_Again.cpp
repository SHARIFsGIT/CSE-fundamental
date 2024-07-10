#include <bits/stdc++.h>
using namespace std;

int main()
{
    int q;
    cin >> q;

    list<int> myList;
    while (q--)
    {
        int position, value;
        cin >> position >> value;

        if (position > myList.size())
        {
            cout << "Invalid" << endl;
            continue;
        }
        else if (position == 0)
        {
            myList.push_front(value);
        }
        else if (position == myList.size())
        {
            myList.push_back(value);
        }
        else
        {
            myList.insert(next(myList.begin(), position), value);
        }

        cout << "L -> ";
        for (auto value : myList)
        {
            cout << value << " ";
        }
        cout << endl;

        cout << "R -> ";
        myList.reverse();
        for (auto value : myList)
        {
            cout << value << " ";
        }
        cout << endl;

        myList.reverse();
    }
    
    return 0;
}