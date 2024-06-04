#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string nm;
    int cls;
    char s;
    long long int id;
    int math_marks;
    int eng_marks;
};

bool compare(Student a, Student b)
{
    if (a.eng_marks != b.eng_marks)
        return a.eng_marks > b.eng_marks;
    else if (a.math_marks != b.math_marks)
        return a.math_marks > b.math_marks;
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
    }

    sort(array, array + N, compare);

    for (int i = 0; i < N; i++)
    {
        cout << array[i].nm << " " << array[i].cls << " " << array[i].s << " " << array[i].id << " " << array[i].math_marks << " " << array[i].eng_marks << endl;
    }
    
    return 0;
}