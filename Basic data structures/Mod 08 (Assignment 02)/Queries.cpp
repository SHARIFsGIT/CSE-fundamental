#include <iostream>
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

void insert_at_head(Node *&head, int value)
{
    Node *newNode = new Node(value);
    newNode->next = head;
    head = newNode;
}

void delete_at_position(Node *&head, int position)
{
    if (head == NULL)
    {
        return;
    }

    if (position == 0)
    {
        Node *deleteNode = head;
        head = head->next;
        delete deleteNode;
        return;
    }

    Node *temp = head;
    for (int i = 0; temp != NULL && i < position - 1; i++)
    {
        temp = temp->next;
    }

    if (temp == NULL || temp->next == NULL)
    {
        return;
    }

    Node *deleteNode = temp->next;
    temp->next = temp->next->next;

    delete deleteNode;
}

void print_linked_list(Node *head)
{
    while (head != NULL)
    {
        cout << head->value << " ";
        head = head->next;
    }
    cout << endl;
}

int main()
{
    Node *head = NULL;

    int Q;
    cin >> Q;

    while (Q--)
    {
        int X, V;
        cin >> X >> V;
        if (X == 0)
        {
            insert_at_head(head, V);
        }
        else if (X == 1)
        {
            insert_at_tail(head, V);
        }
        else if (X == 2)
        {
            if (V >= 0)
            {
                delete_at_position(head, V);
            }
        }
        print_linked_list(head);
    }
    return 0;
}
