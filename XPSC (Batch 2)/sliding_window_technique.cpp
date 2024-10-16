// BruteForce:

/*
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    int k;
    cin >> k;

    int maximum = INT_MIN;
    for (int i = 0; i <= n - k; i++)
    {
        int sum = 0;
        for (int j = i; j < i + k; j++)
        {
            sum += array[j];
        }
        maximum = max(maximum, sum);
    }
    cout << maximum << endl;

    return 0;
}
*/

// Better complexity:

/*
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    int k;
    cin >> k;

    int maximum = INT_MIN;
    int i = 0, j = 0, sum = 0;

    while (j < n)
    {
        if (j < k)
        {
            sum += array[j];
            j++;
        }
        else
        {
            maximum = max(maximum, sum);
            sum -= array[i];
            i++;
            sum += array[j];
            j++;
        }
    }
    cout << maximum << endl;

    return 0;
}
*/

// Best approch:

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    int k;
    cin >> k;

    int maximum = INT_MIN;
    int i = 0, j = 0, sum = 0;

    while (j < n)
    {
        sum += array[j];
        if (j < k - 1)
        {
            j++;
        }
        else
        {
            maximum = max(maximum, sum);
            sum -= array[i];
            i++;
            j++;
        }
    }
    cout << maximum << endl;

    return 0;
}