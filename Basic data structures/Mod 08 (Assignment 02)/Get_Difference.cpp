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

int get_max_element(Node *head)
{
    int maximum = head->value;

    while (head != NULL)
    {
        maximum = max(head->value, maximum);
        head = head->next;
    }
    return maximum;
}

int get_mim_element(Node *head)
{
    int minimum = head->value;

    while (head != NULL)
    {
        minimum = min(head->value, minimum);
        head = head->next;
    }
    return minimum;
}

int main()
{
    Node *head = NULL;
    Node *tail = NULL;

    int value;

    while (true)
    {
        cin >> value;
        if (value == -1)
        {
            break;
        }
        insert_at_tail(head, tail, value);
    }

    cout << get_max_element(head) - get_mim_element(head);

    return 0;
}