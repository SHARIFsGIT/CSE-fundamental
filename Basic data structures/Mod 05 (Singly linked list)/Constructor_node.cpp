#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int value;
    Node *next;
    // Constructor
    Node(int value)
    {
        this->value = value;
        this->next = NULL;
    }
};

int main()
{
    Node a(10), b(20);

    a.next = &b;

    cout << a.value << " " << a.next->value << endl;
    cout << a.value << " " << (*a.next).value << endl;

    return 0;
}