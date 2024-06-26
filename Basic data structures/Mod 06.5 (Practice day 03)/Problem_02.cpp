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

bool has_duplicate(Node *head)
{
    int freq[101] = {0};

    Node *temp = head;
    while (temp != NULL)
    {
        freq[temp->value]++;
        if (freq[temp->value] > 1)
        {
            return true;
        }
        temp = temp->next;
    }
    return false;
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

    cout << (has_duplicate(head) ? "YES" : "NO") << endl;

    return 0;
}