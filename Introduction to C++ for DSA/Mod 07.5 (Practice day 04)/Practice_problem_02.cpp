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
    Student students[n];

    for (int i = 0; i < n; i++)
    {
        cin >> students[i].name >> students[i].roll >> students[i].marks;
    }

    for (int i = 0, j = n - 1; i < j; i++, j--)
    {
        swap(students[i].name, students[j].name);
        swap(students[i].roll, students[j].roll);
        swap(students[i].marks, students[j].marks);
    }

    for (int i = 0; i < n; i++)
    {
        cout << students[i].name << " " << students[i].roll << " " << students[i].marks << endl;
    }

    return 0;
}