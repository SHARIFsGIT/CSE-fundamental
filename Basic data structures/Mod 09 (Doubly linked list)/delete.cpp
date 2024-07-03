#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    Node *previous;
    int value;
    Node *next;

    Node(int value)
    {
        this->previous = NULL;
        this->value = value;
        this->next = NULL;
    }
};

void delete_head(Node *&head)
{
    Node *deleteNode = head;
    head = head->next;
    delete deleteNode;
    head->previous = NULL;
}

void delete_at_position(Node *head, int position)
{
    Node *temp = head;
    for (int i = 0; i < position - 1; i++)
    {
        temp = temp->next;
    }
    Node *deleteNode = temp->next;
    temp->next = temp->next->next;
    temp->next->previous = temp;

    delete deleteNode;
}

void delete_tail(Node *&tail)
{
    Node *deleteNode = tail;
    tail = tail->previous;
    delete deleteNode;
    tail->next = NULL;
}

int size(Node *head)
{
    Node *temp = head;

    int count = 0;
    while (temp != NULL)
    {
        count++;
        temp = temp->next;
    }
    return count;
}

void print_forward(Node *head)
{
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->value << " ";
        temp = temp->next;
    }
    cout << endl;
}

void print_backward(Node *tail)
{
    Node *temp = tail;
    while (temp != NULL)
    {
        cout << temp->value << " ";
        temp = temp->previous;
    }
    cout << endl;
}

int main()
{
    Node *head = new Node(10);
    Node *a = new Node(20);
    Node *b = new Node(30);
    Node *c = new Node(40);
    Node *tail = c;

    head->next = a;
    a->previous = head;
    a->next = b;
    b->previous = a;
    b->next = c;
    c->previous = b;

    int position;
    cin >> position;

    if (position >= size(head))
    {
        cout << "Invalid" << endl;
    }
    else if (position == 0)
    {
        delete_head(head);
    }
    else if (position == size(head) - 1)
    {
        delete_tail(tail);
    }
    else
    {
        delete_at_position(head, position);
    }

    print_forward(head);
    print_backward(tail);

    return 0;
}

/*

===================================Array===================================
Insert head     : O(N)
Insert position : O(N)
Insert tail     : O(1)
Delete head     : O(N)
Delete position : O(N)
Delete tail     : O(1)

====================================SLL====================================
Insert head     : O(1)
Insert position : O(N)
Insert tail     : O(1) / O(N)
Delete head     : O(1)
Delete position : O(N)
Delete tail     : O(N)

====================================DLL====================================
Insert head     : O(1)
Insert position : O(N)
Insert tail     : O(1)
Delete head     : O(1)
Delete position : O(N)
Delete tail     : O(1)

*/