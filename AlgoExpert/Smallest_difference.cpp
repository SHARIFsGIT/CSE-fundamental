/*

#include <vector>
using namespace std;

vector<int> smallestDifference(vector<int> arrayOne, vector<int> arrayTwo)
{

    sort(arrayOne.begin(), arrayOne.end());
    sort(arrayTwo.begin(), arrayTwo.end());

    int i = 0;
    int j = 0;
    int smallest = INT_MAX;

    vector<int> result;

    while (i < arrayOne.size() && j < arrayTwo.size())
    {
        int firstNum = arrayOne[i];
        int secondNum = arrayTwo[j];

        int diff = abs(firstNum - secondNum);

        if (diff < smallest)
        {
            smallest = diff;
            result = {firstNum, secondNum};
        }

        if (firstNum < secondNum)
            i++;
        else if (secondNum < firstNum)
            j++;
        else
            return {firstNum, secondNum};
    }

    return result;
}

*/