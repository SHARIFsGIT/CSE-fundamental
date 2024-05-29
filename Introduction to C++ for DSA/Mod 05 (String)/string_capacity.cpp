#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str = "Hello, world, I'm a programmer? What about you?";
    cout << str.size() << endl;
    cout << str.max_size() << endl;
    cout << str.capacity() << endl;
    cout << str << endl;
    str.resize(10);
    cout << str << endl;
    str.resize(15, 'H');
    cout << str << endl;
    str.clear();
    cout << str.size() << endl;
    (str.empty() == true) ? cout << "Empty" << endl : cout << "Full" << endl;

    return 0;
}