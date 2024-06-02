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

    // Static memory
    Student array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i].name >> array[i].roll >> array[i].marks;
    }

    Student minimum;
    minimum.marks = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        if (array[i].marks < minimum.marks)
        {
            minimum = array[i];
        }
    }
    cout << minimum.name << " " << minimum.roll << " " << minimum.marks << endl;

    Student maximum;
    maximum.marks = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        if (array[i].marks > maximum.marks)
        {
            maximum = array[i];
        }
    }
    cout << maximum.name << " " << maximum.roll << " " << maximum.marks << endl;

    return 0;
}