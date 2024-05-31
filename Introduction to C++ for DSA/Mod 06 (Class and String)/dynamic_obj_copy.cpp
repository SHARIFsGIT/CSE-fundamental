#include <bits/stdc++.h>
using namespace std;

class Person
{
public:
    string name;
    int age;

    Person(string name, int age)
    {
        this->name = name;
        this->age = age;
    }
};

int main()
{
    Person *raju = new Person("Raju", 25);
    Person *saju = new Person("Saju", 35);

    // raju = saju; //don't do

    // raju->name = saju->name;
    // raju->age = saju->age;
    
    *raju = *saju;
    delete saju;

    cout << raju->name << " " << raju->age << endl;

    return 0;
}