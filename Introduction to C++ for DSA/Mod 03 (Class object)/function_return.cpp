#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    int roll;
    int reading;
    double gpa;

    Student(int roll, int reading, double gpa)
    {
        this->roll = roll;
        this->reading = reading;
        this->gpa = gpa;
    }
};

Student *func()
{
    // Student rahim(35, 4, 4.99);
    Student *pointer = new Student(35, 4, 4.99);
    // Student* p = &rahim;

    // return p;
    return pointer;
}

int main()
{
    Student *ans = func();
    // cout << ans.roll << " " << ans.reading << " " << ans.gpa << endl;
    cout << (*ans).roll << " " << ans->reading << " " << ans->gpa << endl;
    delete ans;
    cout << (*ans).roll << " " << ans->reading << " " << ans->gpa << endl;
    return 0;
}