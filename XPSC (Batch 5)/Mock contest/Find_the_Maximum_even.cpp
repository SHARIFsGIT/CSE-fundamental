#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> array(n);
    vector<int> evens, odds;

    for (int i = 0; i < n; i++)
    {
        cin >> array[i];

        if (array[i] % 2 == 0)
        {
            evens.push_back(array[i]);
        }
        else
        {
            odds.push_back(array[i]);
        }
    }

    sort(evens.begin(), evens.end());
    reverse(evens.begin(), evens.end());

    sort(odds.begin(), odds.end());
    reverse(odds.begin(), odds.end());

    int max_even = 0;
    if (!evens.empty())
    {
        max_even = evens[0];
    }

    int max_even_sum = 0;
    if (evens.size() > 1)
    {
        max_even_sum = evens[0] + evens[1];
    }

    int max_odd_sum = 0;
    if (odds.size() > 1)
    {
        max_odd_sum = odds[0] + odds[1];
    }

    int result = max_even;
    if (max_even_sum > result)
    {
        result = max_even_sum;
    }

    if (max_odd_sum > result)
    {
        result = max_odd_sum;
    }

    cout << result << endl;

    return 0;
}
