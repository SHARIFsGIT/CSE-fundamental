#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string name;
    int roll;
    double marks;
};

bool compare(Student a, Student b)
{
    // // if (a.marks <= b.marks)
    // // {
    // //     return true;
    // // }
    // // else
    // // {
    // //     return false;
    // // }

    // // OR:
    // // return a.marks >= b.marks;

    // if (a.marks > b.marks)
    // {
    //     return true;
    // }
    // else if (a.marks < b.marks)
    // {
    //     return false;
    // }
    // else
    // {
    //     // if (a.roll < b.roll)
    //     // {
    //     //     return true;
    //     // }
    //     // else
    //     // {
    //     //     return false;
    //     // }

    //     // OR:
    //     return a.roll < b.roll;
    // }

    // OR:

    if (a.marks == b.marks)
    {
        return a.roll < b.roll;
    }
    else
    {
        return a.marks > b.marks;
    }
}

int main()
{
    int n;
    cin >> n;

    Student array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i].name >> array[i].roll >> array[i].marks;
    }

    sort(array, array + n, compare);

    for (int i = 0; i < n; i++)
    {
        cout << array[i].name << " " << array[i].roll << " " << array[i].marks << endl;
    }
    return 0;
}