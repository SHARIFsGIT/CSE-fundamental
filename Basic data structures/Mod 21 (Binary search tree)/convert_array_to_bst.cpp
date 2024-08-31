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

Node *convert(int array[], int n, int left, int right)
{
    if (left > right)
    {
        return NULL;
    }

    int mid = (left + right) / 2;

    Node *root = new Node(array[mid]);

    Node *left_root = convert(array, n, left, mid - 1);
    Node *right_root = convert(array, n, mid + 1, right);

    root->left = left_root;
    root->right = right_root;

    return root;
}

void level_order(Node *root)
{
    if (root == NULL)
    {
        cout << "Tree is empty" << endl;
        return;
    }

    queue<Node *> queue;
    queue.push(root);

    while (!queue.empty())
    {
        // 1. Keep separate the front value of queue
        Node *front = queue.front();
        queue.pop();

        // 2. Do work with the seperated value
        cout << front->value << " ";

        // 3. Keep the child
        if (front->left != NULL)
        {
            queue.push(front->left);
        }
        if (front->right)
        {
            queue.push(front->right);
        }
    }
}

int main()
{
    int n;
    cin >> n;

    int array[n];
    for (int i = 0; i < n; i++)
    {
        cin >> array[i];
    }

    Node *root = convert(array, n, 0, n - 1);

    level_order(root);

    return 0;
}