CS163 at CCUT Week 4: Final Week!
======
![Matrix](matrix.jpg)

Last Week
-----
Last week we implemented a number of linear linked list functions together. For instance here is our sortedInsert function:

```c++
void sortedInsert(node *&head, int data)
{   // Pass head by reference because head might change
    if(!head)             // Base case
    {
        head = new node;
        head->data = data;
        head->next = NULL;
    }
    else
    {
        node * temp = new node;
        temp->data = data;
        if(data < head->data)
        {
            temp->next = head;
            head = temp;
        }
        else              // Recursive case
            sortedInsert(head->next, data);
    }
}
```

We ended class before we could finish debugging the code for a function which takes a linear linked list and an int $n$, and deletes all occurrences of $n$ from the list recursively. Here is that code. Try to find our mistake and correct it!

```c++
bool deleteAllN(node *&head, int N)
{
    if(!head)
        return false;
    else
    {
        if(N == head->data)
        {
            node * temp = head->next;
            delete head;
            head = NULL;
            head = temp;
        }
        deleteAllN(head->next, N);
    }
    return true;
}
```
