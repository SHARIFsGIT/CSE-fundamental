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

void remove_duplicate(Node *head)
{
    Node *temp = head;

    while (temp != NULL)
    {
        Node *check = temp;
        while (check->next != NULL)
        {
            if (temp->value == check->next->value)
            {
                Node *duplicate = check->next;
                check->next = check->next->next;

                delete duplicate;
            }
            else
            {
                check = check->next;
            }
        }
        temp = temp->next;
    }
}

void print_list(Node *head)
{
    while (head)
    {
        cout << head->value << " ";
        head = head->next;
    }
    cout << endl;
}

int main()
{
    Node *head = NULL;
    Node *tail = NULL;

    int value;
    
    while (cin >> value && value != -1)
    {
        insert_at_tail(head, tail, value);
    }

    remove_duplicate(head);
    print_list(head);

    return 0;
}