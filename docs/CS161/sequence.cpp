#include <iostream>

using namespace std;

int main()
{
	int x = 0;
	for(int i = 0; i < 1000000000; ++i)		// Loop a bunch
		x += 1;
	cout << x;
	
	char y;			// Hack to keep the window open until enter pressed...
	cin.get(y);
	return 0;
}