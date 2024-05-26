#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string name;
    int roll;
    char section;
    double math_marks;
    int cls;

    Student(string name, int roll, char section, double math_marks, int cls)
    {
        this->name = name;
        this->roll = roll;
        this->section = section;
        this->math_marks = math_marks;
        this->cls = cls;
    }
};

int main()
{
    Student student1("Andy", 1, 'A', 90.50, 9);
    Student student2("Any", 9, 'B', 90.60, 5);
    Student student3("Dany", 16, 'A', 85.50, 7);

    ((student1.math_marks > student2.math_marks) && (student1.math_marks > student3.math_marks)) ? cout << student1.name : 
    ((student3.math_marks > student1.math_marks) && (student3.math_marks > student2.math_marks)) ? cout << student3.name : 
    cout << student2.name;

    return 0;
}