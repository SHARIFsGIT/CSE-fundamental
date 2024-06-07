#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string name;
    int id;
    int bangla;
    int english;
    int mathematics;

    int total;
    double average;
    string gpa;
    int roll;
};

bool compare(Student a, Student b)
{
    if (a.total > b.total)
    {
        return true;
    }
    else if (a.total < b.total)
    {
        return false;
    }
    else
    {
        if (a.id < b.id)
        {
            return true;
        }
        else
        {
            return false;
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
        cin >> students[i].id >> students[i].name >> students[i].bangla >> students[i].english >> students[i].mathematics;

        students[i].total = students[i].bangla + students[i].english + students[i].mathematics;

        students[i].average = (double)students[i].total / 3;

        if (students[i].average >= 90)
            students[i].gpa = "A+";
        else if (students[i].average >= 80)
            students[i].gpa = "A";
        else if (students[i].average >= 70)
            students[i].gpa = "A-";
        else if (students[i].average >= 60)
            students[i].gpa = "B+";
        else if (students[i].average >= 50)
            students[i].gpa = "B";
        else if (students[i].average >= 40)
            students[i].gpa = "B-";
        else
            students[i].gpa = "F";
    }

    sort(students, students + n, compare);

    cout << "Roll\tID\tName\tBan\tEng\tMath\tTotal\tAvg\tGPA\n";
    cout << "--------------------------------------------------------------------\n";
    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << "\t" << students[i].id << "\t" << students[i].name << "\t" << students[i].bangla << "\t" << students[i].english << "\t" << students[i].english << "\t" << students[i].total << "\t" << setprecision(3) << students[i].average << "%\t" << students[i].gpa << endl;
    }

    return 0;
}
