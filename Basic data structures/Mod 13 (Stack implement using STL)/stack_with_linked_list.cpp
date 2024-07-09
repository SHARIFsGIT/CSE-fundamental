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

class myStack
{
public:
    Node *head = NULL;
    Node *tail = NULL;

    int stack_size = 0;
    void push(int value)
    {
        stack_size++;

        Node *newNode = new Node(value);
        if (head == NULL)
        {
            head = newNode;
            tail = newNode;
            return;
        }
        newNode->previous = tail;
        tail->next = newNode;
        tail = tail->next;
        
    }

    void pop()
    {
        stack_size--;

        Node *deletedNode = tail;
        tail = tail->previous;
        if (tail == NULL)
        {
            head = NULL;
        }
        else
        {
            tail->next = NULL;
        }

        delete deletedNode;
    }

    int top()
    {
        return tail->value;
    }

    int size()
    {
        return stack_size;
    }

    bool empty()
    {
        if (stack_size == 0)
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
    int n;
    cin >> n;

    myStack st;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;

        st.push(x);
    }

    while (!st.empty())
    {
        cout << st.top() << endl;
        st.pop();
    }

    return 0;
}