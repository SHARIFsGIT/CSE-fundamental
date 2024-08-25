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

int max_depth(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }

    int left_sub_tree = max_depth(root->left);
    int right_sub_tree = max_depth(root->right);

    return max(left_sub_tree, right_sub_tree) + 1;
}

int total_nodes(Node *root)
{
    if (root == NULL)
    {
        return 0;
    }

    return total_nodes(root->left) + total_nodes(root->right) + 1;
}

int main()
{
    Node *root = input_tree();

    int height = max_depth(root);
    int nodes = total_nodes(root);

    int perfect_tree = pow(2, height) - 1;

    cout << (nodes == perfect_tree ? "YES" : "NO") << endl;

    return 0;
}