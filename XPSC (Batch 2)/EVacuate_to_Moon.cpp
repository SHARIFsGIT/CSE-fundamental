#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        long long int car, power_station, hour;
        cin >> car >> power_station >> hour;

        vector<long long int> capacity(car), power(power_station);
        for (int i = 0; i < car; i++)
        {
            cin >> capacity[i];
        }
        for (int i = 0; i < power_station; i++)
        {
            cin >> power[i];
        }

        long long int total_power = 0;

        sort(capacity.rbegin(), capacity.rend());
        sort(power.rbegin(), power.rend());

        for (int i = 0, j = 0; i < car && j < power_station; i++, j++)
        {
            if (power[j] * hour > capacity[i])
            {
                total_power += capacity[i];
            }
            else
            {
                total_power += power[j] * hour;
            }
        }

        cout << total_power << endl;
    }

    return 0;
}
