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

void insert_at_head(Node *&head, Node *&tail, int value)
{
    Node *newNode = new Node(value);
    if (head == NULL)
    {
        head = newNode;
        tail = newNode;
        return;
    }

    newNode->next = head;
    head->previous = newNode;

    head = newNode;
}

void insert_at_position(Node *head, int position, int value)
{
    Node *newNode = new Node(value);
    Node *temp = head;

    for (int i = 0; i < position - 1; i++)
    {
        temp = temp->next;
    }
    newNode->next = temp->next;
    temp->next = newNode;

    newNode->next->previous = newNode;
    newNode->previous = temp;
}

void insert_at_tail(Node *&head, Node *&tail, int value)
{
    Node *newNode = new Node(value);
    if (tail == NULL)
    {
        head = newNode;
        tail = newNode;
        return;
    }

    tail->next = newNode;
    newNode->previous = tail;

    tail = tail->next;
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

    // Node *head = NULL, *tail = NULL;

    int position, value;
    cin >> position >> value;

    if (position == 0)
    {
        insert_at_head(head, tail, value);
    }
    else if (position == size(head))
    {
        insert_at_tail(head, tail, value);
    }

    else if (position >= size(head))
    {
        cout << "Invalid position" << endl;
    }
    else
    {
        insert_at_position(head, position, value);
    }

    print_forward(head);
    print_backward(tail);

    return 0;
}