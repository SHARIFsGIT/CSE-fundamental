// 1: Create a Singly Linked List (Take input from user)
// 2: Count the Size of the list
// 3: Display List
// 4: Insertion at Head
// 5: Insertion at Tail
// 6: Insertion at Specific Position
// 7: Deletion at Head
// 8: Deletion at Tail
// 9: Deletion at Specific Position

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

void insert_at_head(Node *&head, int value)
{
    Node *newNode = new Node(value);
    newNode->next = head;
    head = newNode;
}

void insert_at_position(Node *&head, int value, int position)
{
    if (position < 0)
    {
        cout << "Invalid position" << endl;
        return;
    }
    if (position == 0)
    {
        insert_at_head(head, value);
        return;
    }

    Node *newNode = new Node(value);
    Node *temp = head;

    for (int i = 0; i < position - 1; i++)
    {
        if (temp == NULL)
        {
            cout << "Position out of bounds" << endl;
            return;
        }
        temp = temp->next;
    }

    if (temp == NULL)
    {
        cout << "Position out of bounds" << endl;
        return;
    }

    newNode->next = temp->next;
    temp->next = newNode;
}

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

void delete_at_head(Node *&head)
{
    if (head == NULL)
    {
        cout << "The list is already empty." << endl;
        return;
    }

    Node *temp = head;
    head = head->next;
    delete temp;
}

void delete_at_tail(Node *&head)
{
    if (head == NULL)
    {
        cout << "The list is already empty." << endl;
        return;
    }

    if (head->next == NULL)
    {
        delete head;
        head = NULL;
        return;
    }

    Node *temp = head;
    while (temp->next->next != NULL)
    {
        temp = temp->next;
    }
    delete temp->next;
    temp->next = NULL;
}

void delete_at_position(Node *&head, int position)
{
    if (head == NULL)
    {
        cout << "The list is already empty." << endl;
        return;
    }

    if (position < 0)
    {
        cout << "Invalid position" << endl;
        return;
    }

    if (position == 0)
    {
        delete_at_head(head);
        return;
    }

    Node *temp = head;
    for (int i = 0; i < position - 1; i++)
    {
        if (temp == NULL || temp->next == NULL)
        {
            cout << "Position out of bounds" << endl;
            return;
        }
        temp = temp->next;
    }

    Node *node_to_delete = temp->next;
    if (node_to_delete == NULL)
    {
        cout << "Position out of bounds" << endl;
        return;
    }
    temp->next = node_to_delete->next;
    delete node_to_delete;
}

void print_linked_list(Node *head)
{
    Node *temp = head;

    while (temp != NULL)
    {
        cout << temp->value << " ";
        temp = temp->next;
    }
    cout << endl;
}

int count_size(Node *head)
{
    int count = 0;
    Node *temp = head;

    while (temp != NULL)
    {
        count++;
        temp = temp->next;
    }
    return count;
}

int main()
{
    Node *head = NULL;

    int value;

    cout << "Enter values to create a linked list [enter -1 to end]: ";
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
    cout << "Your linked list: ";
    print_linked_list(head);
    cout << endl;

    int size = count_size(head);
    cout << "Size of linked list: " << size << endl;

    cout << "====================================================" << endl;
    cout << endl;

    cout << "Enter a value to insert at the head: ";
    cin >> value;
    insert_at_head(head, value);

    cout << "Linked List after insertion at head: ";
    print_linked_list(head);
    cout << endl;

    size = count_size(head);
    cout << "Size of the list after insertion: " << size << endl;

    cout << "====================================================" << endl;
    cout << endl;

    int position;
    cout << "Enter a value to insert at a specific position: ";
    cin >> value;

    cout << "Enter the position (starting from 0): ";
    cin >> position;
    insert_at_position(head, value, position);

    cout << "Linked List after insertion at position " << position << ": ";
    print_linked_list(head);
    cout << endl;

    size = count_size(head);
    cout << "Size of the list after insertion: " << size << endl;

    cout << "====================================================" << endl;
    cout << endl;

    cout << "Deleting the head node..." << endl;
    delete_at_head(head);

    cout << "Linked List after deletion at head: ";
    print_linked_list(head);
    cout << endl;

    size = count_size(head);
    cout << "Size of the list after deletion: " << size << endl;

    cout << "====================================================" << endl;
    cout << endl;

    cout << "Enter the position to delete (starting from 0): ";
    cin >> position;
    delete_at_position(head, position);

    cout << "Linked List after deletion at position " << position << ": ";
    print_linked_list(head);
    cout << endl;

    size = count_size(head);
    cout << "Size of the list after deletion: " << size << endl;

    cout << "====================================================" << endl;
    cout << endl;

    cout << "Deleting the tail node..." << endl;
    delete_at_tail(head);

    cout << "Linked List after deletion at tail: ";
    print_linked_list(head);
    cout << endl;

    size = count_size(head);
    cout << "Size of the list after deletion: " << size << endl;

    return 0;
}
