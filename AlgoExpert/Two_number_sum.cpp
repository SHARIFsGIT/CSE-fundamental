/*
---------------------- Brute force | Nested loop -----------------------

#include <vector>
using namespace std;

// Time: O(n^2) | Space: O(1)

vector<int> twoNumberSum(vector<int> array, int targetSum)
{
    for (int i = 0; i < array.size() - 1; i++) // O(n)
    {
        for (int j = i + 1; j < array.size(); j++) // O(n)
        {
            if (array[i] + array[j] == targetSum)
            {
                return {array[i], array[j]};
            }
        }
    }
    return {};
}

*/

/*
-------------------------- Two pointers array --------------------------

#include <vector>
using namespace std;

// Time: O(log(n)) | Space: O(1)

vector<int> twoNumberSum(vector<int> array, int targetSum)
{
    sort(array.begin(), array.end()); // O(log(n))

    int left = 0;
    int right = array.size() - 1;

    while (left < right) // O (n)
    {
        if (array[left] + array[right] == targetSum)
        {
            return {array[left], array[right]};
        }
        else if (array[left] + array[right] < targetSum)
        {
            left++;
        }
        else if (array[left] + array[right] > targetSum)
        {
            right--;
        }
    }
    return {};
}

*/