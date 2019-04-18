#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

struct node
{
	int data;
	node *next;
};

void insert(node *&head, int data)
{
	if(head == NULL)
	{
		head = new node;
		head->data = data;
	}
	else
		insert(head->next, data);
}

void display(node *head)
{
	if(head == NULL)
		return;
	cout << head->data << " -> ";
	display(head->next);
}



int main()
{
	node *head = NULL;
	srand(time(NULL));
	int num = 0;

	for(int i = 0; i < 10; ++i)
	{
		num = rand() % 101;
		cout << num << " ";
		insert(head, num);
		head = NULL;
	}

	display(head);

	return 0;
}
