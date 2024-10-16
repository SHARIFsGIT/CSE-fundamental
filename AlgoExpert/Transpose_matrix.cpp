/*

using namespace std;

// Time: O(n*n) | Space: O(n*n)

vector<vector<int>> transposeMatrix(vector<vector<int>> matrix)
{
    int row = matrix.size();
    int col = matrix[0].size();

    vector<vector<int>> result(col, vector<int>(row));

    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            result[j][i] = matrix[i][j];
        }
    }

    return result;
}

*/