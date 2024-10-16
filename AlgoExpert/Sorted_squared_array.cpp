/*
---------------------------- Brute force -----------------------------

#include <vector>
using namespace std;

// Time: O(nlog(n)) | Space: O(n)

vector<int> sortedSquaredArray(vector<int> array)
{
    vector<int> result(array.size(), 0);

    for (int i = 0; i < array.size(); i++)
    {
        int value = array[i];
        result[i] = value * value;
    }

    sort(result.begin(), result.end());

    return result;
}

*/

/*
--------------------- Range based loop with reference ----------------------

#include <vector>
using namespace std;

// Time: O(nlog(n)) | Space: O(n)

vector<int> sortedSquaredArray(vector<int> array)
{
    for (int &value : array)
    {
        value *= value;
    }

    sort(array.begin(), array.end());

    return array;
}

*/

/*
------------------------ Two pointers method -----------------------

#include <vector>
using namespace std;

// Time: O(n) | Space: O(n)

vector<int> sortedSquaredArray(vector<int> array)
{
    vector<int> result(array.size(), 0);

    int left = 0;
    int right = array.size() - 1;

    for (int i = array.size() - 1; i >= 0; i--)
    {
        if (abs(array[left]) > abs(array[right]))
        {
            result[i] = array[left] * array[left];
            left++;
        }
        else
        {
            result[i] = array[right] * array[right];
            right--;
        }
    }
    return result;
}

*/