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

void insert_at_tail(Node *&head, int value)
{
    Node *newNode = new Node(value);

    if (head == NULL)
    {
        head = newNode;
        return;
    }

    Node *temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = newNode;
}

int get_size(Node *head)
{
    int size = 0;
    Node *temp = head;

    while (temp != NULL)
    {
        size++;
        temp = temp->next;
    }
    return size;
}

void print_middle(Node *head, int size)
{
    if (head == NULL)
    {
        return;
    }

    Node *temp = head;

    int mid1 = (size - 1) / 2;
    int mid2 = size / 2;

    for (int i = 0; i < mid1; i++)
    {
        temp = temp->next;
    }

    cout << temp->value;

    if (mid1 != mid2)
    {
        cout << " " << temp->next->value;
    }
}

int main()
{
    Node *head = NULL;

    int value;

    while (true)
    {
        cin >> value;

        if (value != -1)
        {
            insert_at_tail(head, value);
        }
        else
        {
            break;
        }
    }
    int size = get_size(head);

    print_middle(head, size);

    return 0;
}