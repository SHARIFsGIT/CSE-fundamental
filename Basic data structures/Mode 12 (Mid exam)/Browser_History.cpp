#include <iostream>
#include <sstream>
using namespace std;

class Node
{
public:
    Node *previous;
    string address;
    Node *next;
    Node(string address)
    {
        this->previous = NULL;
        this->address = address;
        this->next = NULL;
    }
};

void insert_at_tail(Node *&head, Node *&tail, string address)
{
    Node *newNode = new Node(address);
    if (head == NULL)
    {
        head = newNode;
        tail = newNode;
        return;
    }
    tail->next = newNode;
    newNode->previous = tail;
    tail = newNode;
}

Node *find_node(Node *head, string address)
{
    Node *temp = head;
    while (temp != NULL)
    {
        if (temp->address == address)
        {
            return temp;
        }
        temp = temp->next;
    }
    return 0;
}

int main()
{
    Node *head = NULL;
    Node *tail = NULL;
    string address;

    while (cin >> address && address != "end")
    {
        insert_at_tail(head, tail, address);
    }

    Node *current = head;
    int q;
    cin >> q;
    cin.ignore();

    while (q--)
    {
        string str;
        getline(cin, str);

        stringstream ss(str);
        string word, addr;

        ss >> word;
        if (word == "visit")
        {
            ss >> addr;
            Node *foundNode = find_node(head, addr);
            if (foundNode)
            {
                current = foundNode;
                cout << current->address << endl;
            }
            else
            {
                cout << "Not Available" << endl;
            }
        }
        else if (word == "next")
        {
            if (current->next)
            {
                current = current->next;
                cout << current->address << endl;
            }
            else
            {
                cout << "Not Available" << endl;
            }
        }
        else if (word == "prev")
        {
            if (current->previous)
            {
                current = current->previous;
                cout << current->address << endl;
            }
            else
            {
                cout << "Not Available" << endl;
            }
        }
    }

    return 0;
}
