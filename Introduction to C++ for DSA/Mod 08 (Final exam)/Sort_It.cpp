#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string nm;
    int cls;
    char s;
    int id;
    int math_marks;
    int eng_marks;
    int total_marks = 0;
};

bool compare(Student a, Student b)
{
    if (a.total_marks > b.total_marks)
        return true;
    else if (a.total_marks < b.total_marks)
        return false;
    else
        return a.id < b.id;
}

int main()
{
    int N;
    cin >> N;

    Student array[N];
    for (int i = 0; i < N; i++)
    {
        cin >> array[i].nm >> array[i].cls >> array[i].s >> array[i].id >> array[i].math_marks >> array[i].eng_marks;

        array[i].total_marks = array[i].math_marks + array[i].eng_marks;
    }

    sort(array, array + N, compare);

    for (int i = 0; i < N; i++)
    {
        cout << array[i].nm << " " << array[i].cls << " " << array[i].s << " " << array[i].id << " " << array[i].math_marks << " " << array[i].eng_marks << endl;
    }
    return 0;
}