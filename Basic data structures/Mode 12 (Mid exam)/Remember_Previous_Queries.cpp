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
        if (position == 0)
        {
            myList.push_front(value);
        }
        else if (position == 1)
        {
            myList.push_back(value);
        }
        else if (position == 2)
        {
            if (value >= 0 && value < myList.size())
            {
                myList.erase(next(myList.begin(), value));
            }
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