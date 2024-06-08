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
    if (a.marks > b.marks)
    {
        return true;
    }
    else if (a.marks < b.marks)
    {
        return false;
    }
    else
    {
        if (a.roll > b.roll)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
}

int main()
{
    int n;
    cin >> n;
    Student students[n];

    for (int i = 0; i < n; i++)
    {
        cin >> students[i].name >> students[i].roll >> students[i].marks;
    }

    sort(students, students + n, compare);

    for (int i = 0; i < n; i++)
    {
        cout << students[i].name << " " << students[i].roll << " " << students[i].marks << endl;
    }

    return 0;
}