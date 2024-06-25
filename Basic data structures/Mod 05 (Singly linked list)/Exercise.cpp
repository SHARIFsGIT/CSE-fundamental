/* 
1. Why do you think linked-list requires more memory than an array when storing the same number of elements?

Linked lists require more memory than arrays because each node in a linked list needs to store an additional pointer/reference to the next node, besides the actual data. In contrast, arrays store elements contiguously and only need memory for the data elements.
*/



/* 
2. Write down Three Limitations of the array which can be solved by the use of Linked List?

a. Fixed Size: Arrays have a fixed size defined at the time of creation. Linked lists can grow and shrink dynamically as elements are added or removed.

b. Insertion and Deletion: Inserting or deleting elements in an array requires shifting elements, which can be inefficient. Linked lists allow efficient insertion and deletion at any position without the need to shift elements.

c. Memory Utilization: Arrays can lead to memory wastage if their size is overestimated. Linked lists allocate memory as needed, leading to potentially more efficient memory usage.
*/



/* 
3. What is the value of Head?

The value of Head is the address of the first node in the linked list. From the diagram, Head points to the first node with value 5 and address 1000.
*/



/* 
4. What is the value of ? marked address location?

The ? marked address location corresponds to the next node after 1020, which points to 1020. So the address is 1020.
*/



/* 
5. What will be the value of Head->Next->Next->Value?

Head points to the first node (value 5).
Head->Next points to the second node (value 7).
Head->Next->Next points to the third node (value 1).
So, Head->Next->Next->Value is 1.

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

int main()
{
    Node *head = new Node(5);
    Node *a = new Node(7);
    Node *b = new Node(1);
    Node *c = new Node(14);
    Node *d = new Node(3);
    Node *e = new Node(11);

    head->next = a;
    a->next = b;
    b->next = c;
    c->next = d;
    d->next = e;

    cout << head->value << " " << head->next->value << " " << head->next->next->value << endl;

    return 0;
}
*/



/* 
6. What will be the value of Sum following pseudocode snippets?

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

int main()
{
    Node *head = new Node(5);
    Node *a = new Node(7);
    Node *b = new Node(1);
    Node *c = new Node(14);
    Node *d = new Node(3);
    Node *e = new Node(11);

    head->next = a;
    a->next = b;
    b->next = c;
    c->next = NULL;
    d->next = e;
    e->next = NULL;

    Node *temp = head;
    while (temp != NULL)
    {
        cout << temp->value << " ";
        temp = temp->next;
    }

    cout << endl;

    int sum = 0;
    temp = head;

    while (temp->next != NULL)
    {
        sum += temp-> value;
        temp = temp -> next;
    }

    sum -= temp -> value;

    cout << "Sum of 1020: " << sum << endl;

    return 0;
}
*/