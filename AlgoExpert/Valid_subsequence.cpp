/*

using namespace std;

// Time: O(n) | Space: O(1)

bool isValidSubsequence(vector<int> array, vector<int> sequence)
{
    int seq_index = 0;
    for (int value : array)
    {
        if (value == sequence[seq_index])
        {
            seq_index++;
            if (seq_index == sequence.size())
            {
                return true;
            }
        }
    }
    return false;
}

*/