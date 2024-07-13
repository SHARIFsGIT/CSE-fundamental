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

class Stack
{
    Node *head = NULL;
    Node *tail = NULL;

    int list_size = 0;

public:
    void push(int value)
    {
        list_size++;

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
        list_size--;

        Node *deleteNode = tail;
        tail = tail->previous;
        if (tail == NULL)
        {
            head = NULL;
            return;
        }
        tail->next = NULL;
        delete deleteNode;
    }

    int top()
    {
        return tail->value;
    }

    int size()
    {
        return list_size;
    }

    bool empty()
    {
        return list_size == 0;
    }
};

class Queue
{
    Node *head = NULL;
    Node *tail = NULL;

    int list_size = 0;

public:
    void push(int value)
    {
        list_size++;

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
        list_size--;

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
        return list_size;
    }

    bool empty()
    {
        return list_size == 0;
    }
};

int main()
{
    Stack st;
    int n;
    cin >> n;

    Queue q;
    int m;
    cin >> m;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        st.push(x);
    }

    for (int i = 0; i < m; i++)
    {
        int value;
        cin >> value;
        q.push(value);
    }

    bool flag = true;
    if (m != n)
        flag = false;
    else
    {
        while (!st.empty())
        {
            if (st.top() != q.front())
            {
                flag = false;
                break;
            }
            st.pop();
            q.pop();
        }
    }

    cout << (flag ? "YES" : "NO") << endl;

    return 0;
}