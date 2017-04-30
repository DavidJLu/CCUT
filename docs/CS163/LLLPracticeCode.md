CS163 at CCUT: Linear Linked List Practice code
======

Here is some of the code that we write together in class. You may copy this and practice writing functions that manipulate linear linked lists.

The following code will randomly generate a list of size `LIST_SIZE` containing ints in the range 0 to `MAX_NUM`. It will then print the list to `stdout`.

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
``` C++
struct node
{
  int data;
  node * next;
};

void insert(node *&head, int data) \\ Insert at front of list
{
  node * temp = new node;
  temp->data = data;
  temp->next = head;
  head = temp;
}

void display(node * head)
{
  if(head == NULL)
    return;
  cout << head->data << "->";
  display(head->next);
}
```
