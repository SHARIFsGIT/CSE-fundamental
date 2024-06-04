#include <bits/stdc++.h>
using namespace std;

class Student
{
public:
    string nm;
    int cls;
    char s;
    int id;
};

int main()
{
    int N;
    cin >> N;

    Student array[N];
    for (int i = 0; i < N; i++)
    {
        cin >> array[i].nm >> array[i].cls >> array[i].s >> array[i].id;
    }

    int i = 0, j = N - 1;
    while (i < j)
    {
        swap(array[i].s, array[j].s);
        i++;
        j--;
    }
    
    for (int i = 0; i < N; i++)
    {
        cout << array[i].nm << " " << array[i].cls << " " << array[i].s << " " << array[i].id << endl;
    }
    return 0;
}