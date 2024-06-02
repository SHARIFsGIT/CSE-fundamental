#include <bits/stdc++.h>
using namespace std;

class Frequency
{
public:
    char item;
    int counter;
};

bool compare(Frequency a, Frequency b)
{
    if (a.counter == b.counter)
    {
        return a.item < b.item;
    }
    else
    {
        return a.counter > b.counter;
    }
}

int main()
{
    string str;
    cin >> str;

    Frequency charecters[26];
    for (int i = 0; i < 26; i++)
    {
        charecters[i].item = char(i + 'a');
        charecters[i].counter = 0;
    }

    for (char c : str)
    {
        int ascii = int(c - 'a');
        charecters[ascii].counter++;
    }

    sort(charecters, charecters + 26, compare);

    for (int i = 0; i < 26; i++)
    {
        for (int j = 0; j < charecters[i].counter; j++)
        {
            cout << charecters[i].item;
        }
    }

    return 0;
}