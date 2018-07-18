// MaxValue.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int maxElement(int arr[], int len)
{
	int max = max = arr[0];
	for (int i = 0; i < len; i++)
	{
		if (arr[i]>max)
		{
			max = arr[i];
		}
	}
	return max;
}

int main()
{
	
	int len = 0;
	cout << "Enter number of data values:";
	cin >> len ;
	int* arr = new int[len];
	int n = 0;
	for (int i = 0; i < len; i++)
	{
		cout << "Enter value smaller than 2,147,483,647" << i+1 << ":"<< endl;
		cin >> n;
		arr[i] = n;
	}
		
	cout << "The max is " << maxElement(arr, len) << endl;
	
    return 0;
}

