#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    Node *previous;
    int value;
    Node *next;

    Node(int value) {
        this->previous = NULL;
        this->value = value;
        this->next = NULL;
    }
};

void insert_at_tail(Node *&head, Node *&tail, int value) {
    Node *newNode = new Node(value);
    if (tail == NULL) {
        head = newNode;
        tail = newNode;
        return;
    }
    tail->next = newNode;
    newNode->previous = tail;
    tail = newNode;
}

int get_size(Node *head) {
    int size = 0;
    while (head != NULL) {
        size++;
        head = head->next;
    }
    return size;
}

bool same(Node *head1, Node *head2) {
    if (get_size(head1) != get_size(head2)) {
        return false;
    }
    Node *temp1 = head1;
    Node *temp2 = head2;
    while (temp1 != NULL) {
        if (temp1->value != temp2->value) {
            return false;
        }
        temp1 = temp1->next;
        temp2 = temp2->next;
    }
    return true;
}

void read_list(Node *&head, Node *&tail) {
    int value;
    while (cin >> value && value != -1) {
        insert_at_tail(head, tail, value);
    }
}

int main() {
    Node *head1 = NULL, *tail1 = NULL;
    Node *head2 = NULL, *tail2 = NULL;

    read_list(head1, tail1);
    read_list(head2, tail2);

    cout << (same(head1, head2) ? "YES" : "NO") << endl;

    return 0;
}
