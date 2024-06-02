#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string name;
    int roll;
    double marks;
};

int main()
{
    int n;
    cin >> n;

    Student array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i].name >> array[i].roll >> array[i].marks;
    }

    // Selection sort ascending order
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (array[i].marks > array[j].marks)
            {
                swap(array[i], array[j]);
            }
            else if (array[i].marks == array[j].marks)
            {
                if (array[i].roll > array[j].roll)
                {
                    swap(array[i], array[j]);
                }
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout << array[i].name << " " << array[i].roll << " " << array[i].marks << endl;
    }

    return 0;
}