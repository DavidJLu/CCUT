#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;



int main()
{

	srand(time(NULL));
	int num = 0;
	
	for(int i = 0; i < 10; ++i)
	{
		num = rand() % 101;
		cout << num << " ";

	}


	return 0;
}