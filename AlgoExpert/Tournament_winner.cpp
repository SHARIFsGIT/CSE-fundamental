/*

#include <vector>
using namespace std;

// Time: O(n) | Space: O(n)

string tournamentWinner(vector<vector<string>> competitions, vector<int> results)
{
    map<string, int> mp;

    for (int i = 0; i < results.size(); i++)
    {
        if (results[i])
        {
            mp[competitions[i][0]]++;
        }
        else
        {
            mp[competitions[i][1]]++;
        }
    }

    int points = 0;
    string winner;

    for (auto it : mp)
    {
        if (it.second > points)
        {
            winner = it.first;
            points = it.second;
        }
    }

    return winner;
}

*/