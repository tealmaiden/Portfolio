// pointerTutorial.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "pointerTutorial.h"

int *sortAsc(int *p, int n) 
{
	int i, j;
	for (i = 0; i<n; i++)
		for (j = i + 1; j<n; j++)
			if (*(p + j)<*(p + i))
			{
				int temp = *(p + j);
				*(p + j) = *(p + i);
				*(p + i) = temp;
			}

	return p;
}

int main()
{
	//sort:
	int arr[] = { 23,34,2,3,5,12,42,56,89,8 };
	int *p = sortAsc(arr, 10);
	//output the sorted array ascending:
	int i;
	for (i = 0; i < 10; i++)
	{
		cout << "sort ascending: " << *(p + i) << endl;
	}
	//output the sorted array ascending: descending
	for (i = 9; i >= 0; i--)
	{
		cout << "sort descending: " << *(p + i) << endl;
	}	

    return 0;
}

