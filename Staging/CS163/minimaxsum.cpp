#include <iostream>

using namespace std;

long int findMax(long int *arr, int len)
{
    long int max = arr[0];
    for(int i = 1; i < len; ++i)
    {
        if(arr[i] > max)
            max = arr[i];
    }
    return max;
}

long int findMin(long int *arr, int len)
{
    long int min = arr[0];
    for(int i = 1; i < len; ++i)
    {
        if(arr[i] < min)
            min = arr[i];
    }
    return min;
}


int main()
{
    long int a;
    long int b;
    long int c;
    long int d;
    long int e;
    cin >> a >> b >> c >> d >> e;

    long int arr[5] = {a, b, c, d, e};

    long int min = findMin(arr, 5);
    long int max = findMax(arr, 5);
    long int sum = a + b + c + d + e;
    cout << sum - max << " " << sum - min;


    return 0;
}
