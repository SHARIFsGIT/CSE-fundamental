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

void insert_tail(Node *&head, Node *&tail, int value)
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

void size_check(Node *head1, Node *head2)
{
    int size1 = get_size(head1);
    int size2 = get_size(head2);

    cout << ((size1 == size2) ? "YES" : "NO") << endl;
}

void read_list(Node *&head, Node *&tail)
{
    int value;
    while (cin >> value && value != -1)
    {
        insert_tail(head, tail, value);
    }
}

int main()
{
    Node *head1 = NULL, *tail1 = NULL;
    Node *head2 = NULL, *tail2 = NULL;

    read_list(head1, tail1);
    read_list(head2, tail2);

    size_check(head1, head2);

    return 0;
}