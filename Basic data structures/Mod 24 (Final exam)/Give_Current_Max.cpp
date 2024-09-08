#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string name;
    int roll;
    int marks;

    Student(string name, int roll, int marks)
    {
        this->name = name;
        this->roll = roll;
        this->marks = marks;
    }
};

class compare
{
public:
    bool operator()(Student a, Student b)
    {
        if (a.marks != b.marks)
        {
            return a.marks < b.marks;
        }
        return a.roll > b.roll;
    }
};

int main()
{
    int n;
    cin >> n;

    priority_queue<Student, vector<Student>, compare> p;

    while (n--)
    {
        string name;
        int roll;
        int marks;

        cin >> name >> roll >> marks;

        Student obj(name, roll, marks);
        p.push(obj);
    }

    int q;
    cin >> q;
    while (q--)
    {
        int a;
        cin >> a;

        if (a == 1)
        {
            if (p.empty())
            {
                cout << "Empty" << endl;
            }
            else
            {
                cout << p.top().name << " " << p.top().roll << " " << p.top().marks << endl;
            }
        }
        else if (a == 2)
        {
            if (!p.empty())
            {
                p.pop();
            }
            if (p.empty())
            {
                cout << "Empty" << endl;
            }
            else
            {
                cout << p.top().name << " " << p.top().roll << " " << p.top().marks << endl;
            }
        }
        else
        {
            string name;
            int roll;
            int marks;

            cin >> name >> roll >> marks;

            Student new_obj(name, roll, marks);
            p.push(new_obj);

            cout << p.top().name << " " << p.top().roll << " " << p.top().marks << endl;
        }
    }
    
    return 0;
}