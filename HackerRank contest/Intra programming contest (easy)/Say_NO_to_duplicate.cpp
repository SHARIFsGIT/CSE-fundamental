#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        {
            int n;
            cin >> n;

            int array[n];
            for (int i = 0; i < n; i++)
            {
                cin >> array[i];
            }

            for (int i = 0; i < n - 1; i++)
            {
                for (int j = i + 1; j < n; j++)
                {
                    if (array[i] > array[j])
                    {
                        int temp = array[i];
                        array[i] = array[j];
                        array[j] = temp;
                    }
                }
            }

            int copy_array[n];
            copy_array[0] = array[0];

            int j = 1;
            for (int i = 1; i < n; i++)
            {
                if (array[i] != copy_array[j - 1])
                {
                    copy_array[j++] = array[i];
                }
            }

            for (int i = 0; i < j; i++)
            {
                cout << copy_array[i] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}