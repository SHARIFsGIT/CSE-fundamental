#include <bits/stdc++.h>
using namespace std;

class Pair
{
public:
    string name;
    int number;

    Pair(string name, int number)
    {
        this->name = name;
        this->number = number;
    }
};

/*
class compare
{
public:
    bool operator()(Pair a, Pair b)
    {
        if (a.name > b.name)
        {
            return true;
        }
        else if (a.name < b.name)
        {
            return false;
        }
        else
        {
            if (a.number < b.number)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
    }
};
*/

class compare
{
public:
    bool operator()(Pair a, Pair b)
    {
        if (a.name != b.name)
        {
            return a.name > b.name;
        }
        return a.number < b.number;
    }
};

bool cmp(const Pair &a, const Pair &b)
{
    if (a.name != b.name)
    {
        return a.name < b.name;
    }
    return a.number > b.number;
}

int main()
{
    int n;
    cin >> n;

    vector<Pair> v;
    for (int i = 0; i < n; i++)
    {
        string name;
        int number;

        cin >> name >> number;

        Pair obj(name, number);
        v.push_back(obj);
    }

    sort(v.begin(), v.end(), cmp);

    for (auto element : v)
    {
        cout << element.name << " " << element.number << " " << endl;
    }

    return 0;
}