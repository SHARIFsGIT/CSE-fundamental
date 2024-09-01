#include <bits/stdc++.h>
using namespace std;

class Node
{
public:
    Node *left;
    int value;
    Node *right;

    Node(int value)
    {
        this->left = NULL;
        this->value = value;
        this->right = NULL;
    }
};

Node *input_tree()
{
    int value;
    cin >> value;

    Node *root;
    if (value == -1)
    {
        root = NULL;
    }
    else
    {
        root = new Node(value);
    }

    queue<Node *> queue;
    if (root)
    {
        queue.push(root);
    }

    while (!queue.empty())
    {
        // 1. Keep separate the front value of queue
        Node *parent = queue.front();
        queue.pop();

        // 2. Do work with the seperated value
        int left_value, right_value;
        cin >> left_value >> right_value;

        Node *left_node;
        Node *right_node;

        if (left_value == -1)
        {
            left_node = NULL;
        }
        else
        {
            left_node = new Node(left_value);
        }

        if (right_value == -1)
        {
            right_node = NULL;
        }
        else
        {
            right_node = new Node(right_value);
        }

        parent->left = left_node;
        parent->right = right_node;

        // 3. Keep the child
        if (parent->left)
        {
            queue.push(parent->left);
        }
        if (parent->right)
        {
            queue.push(parent->right);
        }
    }
    return root;
}

void print_left(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    if (root->left)
    {
        print_left(root->left);
        cout << root->value << " ";
    }
    if (root->left == NULL)
    {
        print_left(root->right);
        cout << root->value << " ";
    }
}

void print_right(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    if (root->right)
    {
        cout << root->value << " ";
        print_right(root->right);
    }
    if (root->right == NULL)
    {
        cout << root->value << " ";
        print_right(root->left);
    }
}

int main()
{
    Node *root = input_tree();

    if (root)
    {
        print_left(root->left);
        cout << root->value << " ";
        print_right(root->right);
    }

    return 0;
}