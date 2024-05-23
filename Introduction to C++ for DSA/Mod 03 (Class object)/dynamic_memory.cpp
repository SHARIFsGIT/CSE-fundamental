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

int main()
{
    Student rahim(32, 9, 4.98);
    Student *pointer = new Student(32, 9, 4.98);
    cout << pointer->roll << " " << pointer->reading << " " << pointer->gpa << endl;
    return 0;
}