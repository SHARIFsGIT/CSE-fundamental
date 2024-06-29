#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    int value;
    Node *next;

    Node(int value)
    {
        this->value = value;
        this->next = NULL;
    }
};

void insert_at_tail(Node *&head, Node *&tail, int value)
{
    Node *newNode = new Node(value);
    if (head == NULL)
    {
        head = newNode;
        tail = newNode;
        return;
    }
    tail->next = newNode;
    tail = newNode;
}

bool same_check(Node *head1, Node *head2)
{
    while (head1 && head2)
    {
        if (head1->value != head2->value)
        {
            return false;
        }
        head1 = head1->next;
        head2 = head2->next;
    }
    if (head1 == NULL && head2 == NULL)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void read_list(Node *&head, Node *&tail)
{
    int value;
    while (cin >> value && value != -1)
    {
        insert_at_tail(head, tail, value);
    }
}

int main()
{
    Node *head1 = NULL, *tail1 = NULL;
    Node *head2 = NULL, *tail2 = NULL;

    read_list(head1, tail1);
    read_list(head2, tail2);

    cout << (same_check(head1, head2) ? "YES" : "NO") << endl;

    return 0;
}