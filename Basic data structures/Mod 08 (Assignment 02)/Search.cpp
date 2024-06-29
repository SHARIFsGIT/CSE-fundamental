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

int find_index(Node *head, int value)
{
    int index = 0;

    Node *temp = head;

    while (temp != NULL)
    {
        if (temp->value == value)
        {
            return index;
        }
        temp = temp->next;
        index++;
    }
    return -1;
}

int main()
{
    int test;
    cin >> test;

    for (int i = 0; i < test; i++)
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

        int x;
        cin >> x;

        cout << find_index(head, x) << endl;
    }

    return 0;
}