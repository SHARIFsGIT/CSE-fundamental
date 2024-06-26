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
    Node *new_node = new Node(value);
    if (head == NULL)
    {
        head = new_node;
        cout << endl
             << "Inserted at head" << endl
             << endl;
        return;
    }

    Node *temp = head;
    while (temp->next != NULL)
    {
        temp = temp->next;
    }
    temp->next = new_node;
    cout << endl
         << "Inserted at tail" << endl
         << endl;
}

void print_link_list(Node *head)
{
    cout << endl;
    cout << "Your linked list: ";
    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->value << " ";
        temp = temp->next;
    }
    cout << endl
         << endl;
}

void insert_at_position(Node *head, int position, int value)
{
    Node *newNode = new Node(value);
    Node *tmp = head;
    for (int i = 1; i <= position - 1; i++)
    {
        tmp = tmp->next;
    }
    newNode->next = tmp->next;
    tmp->next = newNode;
    cout << endl
         << endl
         << "Inserted at position " << position << endl
         << endl;
}

void insert_at_head(Node *&head, int value)
{
    Node *newNode = new Node(value);
    newNode->next = head;

    head = newNode;
    cout << endl
         << "Inserted at head " << endl
         << endl;
}

void delete_from_position(Node *head, int position)
{
    Node *tmp = head;
    for (int i = 1; i <= position - 1; i++)
    {
        tmp = tmp->next;
    }
    Node *deleteNode = tmp->next;
    tmp->next = tmp->next->next;
    delete deleteNode;
}

int main()
{
    Node *head = NULL;

    while (true)
    {
        cout << "Option 1: Insert at tail" << endl;
        cout << "Option 2: Print linked list" << endl;
        cout << "Option 3: Insert at any position" << endl;
        cout << "Option 4: Insert at head" << endl;
        cout << "Option 5: Delete from any position" << endl;
        cout << "Option 6: Terminate" << endl;

        int option;
        cin >> option;

        if (option == 1)
        {
            cout << "Please enter value: ";
            int value;
            cin >> value;

            insert_at_tail(head, value);
        }
        else if (option == 2)
        {
            print_link_list(head);
        }
        else if (option == 3)
        {
            int position, value;
            cout << "Enter position: ";
            cin >> position;
            cout << "Enter value: ";
            cin >> value;
            if (position == 0)
            {
                insert_at_head(head, value);
            }
            else
            {
                insert_at_position(head, position, value);
            }
        }
        else if (option == 4)
        {
            int value;
            cout << "Enter value: ";
            cin >> value;

            insert_at_head(head, value);
        }
        else if (option == 5)
        {
            int position;
            cout << "Enter position: ";
            cin >> position;

            delete_from_position(head, position);
        }
        else if (option == 6)
        {
            break;
        }
    }

    return 0;
}