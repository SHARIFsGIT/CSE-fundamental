#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    int roll;
    int reading;
    double gpa;
    
    // Constructor
    // Student(int r, int re, double g)
    // {
    //     roll = r;
    //     reading = re;
    //     gpa = g;
    // }
    Student(int roll, int reading, double gpa)
    {
        this->roll = roll;
        this->reading = reading;
        // this->gpa = gpa;
        (*this).gpa = gpa;
    }
};

int main()
{
    Student rahim(29, 6, 4.69);
    cout << rahim.roll << " " << rahim.reading << " " << rahim.gpa << endl;

    Student karim(2, 9, 4.92);
    cout << karim.roll << " " << karim.reading << " " << karim.gpa << endl;

    return 0;
}