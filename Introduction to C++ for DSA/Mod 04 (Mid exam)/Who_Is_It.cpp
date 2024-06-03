#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    int id;
    char name[100];
    char section;
    double total_marks;
};

int main()
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        Student students[3];

        for (int i = 0; i < 3; i++)
        {
            cin >> students[i].id >> students[i].name >> students[i].section >> students[i].total_marks;
        }

        int max_marks = -1, max_index = -1;
        for (int i = 0; i < 3; i++)
        {
            if ((students[i].total_marks > max_marks) || (students[i].total_marks == max_marks && students[i].id < students[max_index].id))
            {
                max_marks = students[i].total_marks;
                max_index = i;
            }
        }

        cout << students[max_index].id << " " << students[max_index].name << " " << students[max_index].section << " " << students[max_index].total_marks << endl;
    }

    return 0;
}