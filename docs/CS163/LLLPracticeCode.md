CS163 at CCUT: Linear Linked List Practice code
======

Here is some of the code that we wrote together in class. You may copy this and practice writing functions that manipulate linear linked lists.

This code with the functions included will generate a list of size `LIST_SIZE` containing pseudo random ints in the range 0 to `MAX_NUM`. These constants are defined and you can change them. It will then print the list to `stdout`.

-----
#### Main function
```C++
#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

const int LIST_SIZE = 20;
const int MAX_NUM = 101;

int main()
{
  node * head = NULL;

  srand(time(NULL));
  for(int i = 0; i < LIST_SIZE; ++i)
  {
    int temp = rand() % MAX_NUM;
    insert(head, temp);
  }

  display(head); cout << endl;
}
```
-----
#### Some linear linked functions that we wrote together:
```C++
struct node
{
  int data;
  node * next;
};

void insert(node *&head, int data) // Insert at rear of list
{
  if(head == NULL)
  {
    head = new node;
    head->data = data;
  }
  else
    insert(head->next, data);
}

void display(node * head) // Display list from first to last
{
  if(head == NULL)
    return;
  cout << head->data << "->";
  display(head->next);
}
```
