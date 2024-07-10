#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    Node *previous;
    int value;
    Node *next;

    Node(int value)
    {
        this->previous = NULL;
        this->value = value;
        this->next = NULL;
    }
};

class myQueue
{
public:
    Node *head = NULL;
    Node *tail = NULL;

    int size_of_list = 0;
    void push(int value)
    {
        size_of_list++;
        Node *newNode = new Node(value);
        if (head == NULL)
        {
            head = newNode;
            tail = newNode;
            return;
        }

        tail->next = newNode;
        newNode->previous = tail;
        tail = tail->next;
    }

    void pop()
    {
        size_of_list--;
        Node *deleteNode = head;
        head = head->next;
        if (head == NULL)
        {
            tail = NULL;
            delete deleteNode;
            return;
        }
        head->previous = NULL;
        delete deleteNode;
    }

    int front()
    {
        return head->value;
    }

    int size()
    {
        return size_of_list;
    }

    bool empty()
    {
        if (size_of_list == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};

int main()
{
    myQueue q;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;

        q.push(x);
    }

    while (!q.empty())
    {
        cout << q.front() << endl;
        q.pop();
    }

    return 0;
}