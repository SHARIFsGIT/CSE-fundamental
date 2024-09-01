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

int sum(Node *root)
{
    if (root == NULL || (root->left == NULL && root->right == NULL))
    {
        return 0;
    }
    
    return root->value + sum(root->left) + sum(root->right);
}

int main()
{
    Node *root = input_tree();

    cout << sum(root) << endl;

    return 0;
}