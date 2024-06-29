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

void insert_at_index(Node *&head, int index, int value)
{
    int size = get_size(head);
    if (index < 0 || index > size)
    {
        cout << "Invalid" << endl;
        return;
    }

    Node *newNode = new Node(value);

    if (index == 0)
    {
        newNode->next = head;
        head = newNode;
        return;
    }

    Node *temp = head;
    for (int i = 0; i < index - 1; i++)
    {
        temp = temp->next;
    }
    newNode->next = temp->next;
    temp->next = newNode;
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

    int q;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        int index, value;
        cin >> index >> value;

        insert_at_index(head, index, value);

        if (index >= 0 && index <= (get_size(head) - 1))
        {
            print_list(head);
        }
    }

    return 0;
}
