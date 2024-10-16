/*

#include <vector>
#include <algorithm>
using namespace std;

// Time: O(n^3) | Space: O(n^2)
vector<vector<int>> threeNumberSum(vector<int> array, int targetSum)
{
    vector<vector<int>> triplets;

    for (int i = 0; i < array.size() - 2; i++)
    {
        for (int j = i + 1; j < array.size() - 1; j++)
        {
            for (int k = j + 1; k < array.size(); k++)
            {
                int currentSum = array[i] + array[j] + array[k];
                if (currentSum == targetSum)
                {
                    vector<int> triplet = {array[i], array[j], array[k]};

                    sort(triplet.begin(), triplet.end());

                    triplets.push_back(triplet);
                }
            }
        }
    }

    sort(triplets.begin(), triplets.end());

    return triplets;
}

-----------------------------------------------------------------------------------

#include <vector>
#include <algorithm>
using namespace std;

// Time: O(n^2) | Space: O(n)
vector<vector<int>> threeNumberSum(vector<int> array, int targetSum)
{
    sort(array.begin(), array.end());

    vector<vector<int>> triplets;

    for (int i = 0; i < array.size() - 2; i++)
    {
        int left = i + 1;
        int right = array.size() - 1;

        while (left < right)
        {
            int currentSum = array[i] + array[left] + array[right];
            if (currentSum == targetSum)
            {
                triplets.push_back({array[i], array[left], array[right]});
                left++;
                right--;
            }
            else if (currentSum < targetSum)
            {
                left++;
            }
            else
            {
                right--;
            }
        }
    }
    return triplets;
}

*/