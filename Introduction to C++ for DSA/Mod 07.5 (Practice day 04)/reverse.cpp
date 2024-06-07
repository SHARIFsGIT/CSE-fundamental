#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    int id;
    string name;
    int marks;
};

int main()
{
    int n;
    cin >> n;
    Student students[n];

    for (int i = 0; i < n; i++)
    {
        cin >> students[i].id >> students[i].name >> students[i].marks;
    }

    // int i = 0, j = n - 1;
    // while (i < j)
    // {
    //     i++;
    //     j--;
    // }

    // Using for loop:
    for (int i = 0, j = n - 1; i < j; i++, j--)
    {
        swap(students[i].marks, students[j].marks);
    }

    for (int i = 0; i < n; i++)
    {
        cout << students[i].id << " " << students[i].name << " " << students[i].marks << endl;
    }

    return 0;
}