class Solution
{
public:
    vector<vector<int>> dp;

    bool checkSum(int n, int target, vector<int> &arr)
    {
        if (target == 0)
            return true;
        if (n == 0)
            return false;

        if (dp[n][target] != -1)
        {
            return dp[n][target];
        }

        if (arr[n - 1] <= target)
        {
            bool include = checkSum(n - 1, target - arr[n - 1], arr);
            bool exclude = checkSum(n - 1, target, arr);
            return dp[n][target] = include || exclude;
        }
        else
        {
            return dp[n][target] = checkSum(n - 1, target, arr);
        }
    }

    bool isSubsetSum(vector<int> &arr, int target)
    {
        int n = arr.size();
        dp.resize(n + 1, vector<int>(target + 1, -1));
        return checkSum(n, target, arr);
    }
};

/*
https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
*/