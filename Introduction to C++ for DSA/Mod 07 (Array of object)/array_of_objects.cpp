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
    // Student array[n];

    // Dynamic memory
    Student *array = new Student[n];
    for (int i = 0; i < n; i++)
    {
        cin.ignore();
        getline(cin, array[i].name);
        cin >> array[i].roll >> array[i].marks;
    }

    for (int i = 0; i < n; i++)
    {
        cout << array[i].name << " " << array[i].roll << " " << array[i].marks << endl;
    }

    return 0;
}