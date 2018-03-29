CS163 at CCUT: Binary Search Tree Practice Code
======

You may copy this and practice writing functions that manipulate binary search trees.

This code with the functions included will generate a list of up to size `LIST_SIZE` containing pseudo random ints in the range 0 to `MAX_NUM`. These constants are defined and you can change them. It will then print the list to `stdout`.

------
#### Main

```c++
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <queue>

using namespace std;

const int LIST_SIZE = 20;
const int MAX_NUM = 101;

int main()
{
    node * root = NULL;

    srand(time(NULL));
    int list_size = rand() % LIST_SIZE;
    cout << "Inserting in the following order: ";
    for(int i = 0; i < list_size; ++i)
    {
        int temp = rand() % MAX_NUM;
        cout << temp << " ";
        insert(root, temp);
    }

    cout << endl;
    printLevel(root); cout << endl;   // Prints the tree levels
    printInOrder(root); cout << endl; // Prints the items in order

    return 0;
}
```

#### Some BST functions to make the above work:
You can separate this into a .h and .cpp file or you can copy and paste this above the `main()` function.

``` C++
struct node
{
    int data;
    node * left;
    node * right;
};

void insert(node *&root, int data)
{
    if(!root)   // Base case
    {
        root = new node;
        root->data = data;
        root->left = NULL;
        root->right = NULL;
    }
    else    // Compare the data
    {
        if(data < root->data)
            insert(root->left, data);
        else
            insert(root->right, data);
    }
}

void printInOrder(node *root)
{
    if(!root)
        return;
    printInOrder(root->left);
    cout << root->data << " ";
    printInOrder(root->right);
}

int height(node *root)
{
    if(!root)
        return 0;
    else
    {
        int leftH = height(root->left);
        int rightH = height(root->right);
        if(leftH > rightH)
            return leftH + 1;
        else
            return rightH + 1;
    }
}

void printLevel(node *root)
{
    if(!root)
        return;
    int level = 0;
    int h = height(root);
    queue<node*> currentLevel, nextLevel; // Use queue to keep track of what level to print
    currentLevel.push(root);
    cout << (level++) << ": ";
    while(!currentLevel.empty())
    {
        node * currNode = currentLevel.front();
        currentLevel.pop();
        if(currNode)
        {
            cout << currNode->data << " ";
            nextLevel.push(currNode->left);
            nextLevel.push(currNode->right);
        }
        if(currentLevel.empty())
        {
            cout << endl;
            if(level < h)
                cout << (level++) << ": ";
            swap(currentLevel, nextLevel);
        }
    }
}

```
