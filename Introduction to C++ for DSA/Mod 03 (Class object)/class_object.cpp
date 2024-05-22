#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    char name[100];
    int roll;
    double cgpa;
};

int main()
{
    Student a, b;

    cin >> a.name >> a.roll >> a.cgpa;
    cout << "Name: " << a.name << " Roll: " << a.roll << " CGPA: " << a.cgpa << endl;

    getchar();
    cin.getline(b.name, 100);
    cin >> b.roll >> b.cgpa;
    cout << "Name: " << b.name << " Roll: " << b.roll << " CGPA: " << b.cgpa << endl;

    return 0;
}