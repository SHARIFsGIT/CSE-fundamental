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

bool is_sorted(Node *head)
{
    if (head == NULL || head->next == NULL)
    {
        return true;
    }

    Node *temp = head;
    while (temp->next != NULL)
    {
        if (temp->value > temp->next->value)
        {
            return false;
        }
        temp = temp->next;
    }
    return true;
}

void print_list(Node *head)
{
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->value;
        if (temp->next != NULL)
        {
            cout << " ";
        }
        temp = temp->next;
    }
    cout << endl;
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

    cout << (is_sorted(head) ? "YES" : "NO") << endl;

    return 0;
}
