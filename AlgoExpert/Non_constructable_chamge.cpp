/*

#include <vector>
using namespace std;

// Time: O(n log(n)) | Space: O(1)

int nonConstructibleChange(vector<int> coins)
{
    sort(coins.begin(), coins.end());

    int sum = 0;
    for (int coin : coins)
    {
        if (coin > (sum + 1))
        {
            return sum + 1;
        }
        sum += coin;
    }
    return sum + 1;
}

*/