#include <bits/stdc++.h>
using namespace std;

int main()
{
    vector<int> array[2];

    array[0].push_back(1);
    array[0].push_back(2);
    array[0].push_back(3);

    array[1].push_back(1);
    array[1].push_back(2);
    array[1].push_back(3);

    // Getting error cause the array is declared on above is static array
    for (int i = 0; i < array.size(); i++)
    {
        for (int j = 0; j < array[i].size(); j++)
        {
            cout << array[i][j] << " ";
        }
        cout << endl;
    }


    return 0;
}


/*
                    Row dynamic     |       Column dynamic

Array of vector:        No                         Yes

Vector of vector:       Yes                        Yes

*/





/*

vector of vector: vector<vector<int>> a;

vector of array: vector<array<int, 5>> a;

array of vector: vector<int> a[5];

*/