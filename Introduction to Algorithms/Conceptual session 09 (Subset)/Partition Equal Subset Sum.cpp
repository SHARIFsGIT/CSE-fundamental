class Solution {
public:
    int dp[205][20005];

    bool checkSum(int n, int target, vector<int>& arr) {
        if (target == 0)
            return true;
        if (n == 0)
            return false;

        if (dp[n][target] != -1) {
            return dp[n][target];
        }

        if (arr[n - 1] <= target) {
            bool include = checkSum(n - 1, target - arr[n - 1], arr);
            bool exclude = checkSum(n - 1, target, arr);
            return dp[n][target] = include || exclude;
        } else {
            return dp[n][target] = checkSum(n - 1, target, arr);
        }
    }

    bool canPartition(vector<int>& nums) {
        int n = nums.size();
        memset(dp, -1, sizeof(dp));

        int sum = 0;

        for (int child : nums) {
            sum += child;
        }

        if (sum % 2 == 1) {
            return false;
        }

        return checkSum(n, sum / 2, nums);
    }
};

/*
https://leetcode.com/problems/partition-equal-subset-sum/
*/