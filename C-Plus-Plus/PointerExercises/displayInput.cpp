// displayInput.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

int main()
{
	
	//pointer input, display to console
	int arr[5], i;
	int *p = arr;
	cout << "Enter five numbers separated by space:";
	cin >> *p >> *(p + 1) >> *(p + 2) >> *(p + 3) >> *(p + 4);
	cout << "Your numbers in order are:\n";
	for (i = 0; i<5; i++)
	cout << arr[i] << endl;

	//pointer input, display to console reverse
	cout << "Enter five numbers separated by space:";
	cin >> *p >> *(p + 1) >> *(p + 2) >> *(p + 3) >> *(p + 4);
	cout << "Your numbers in reverse order are:\n";
	for (i = 4; i>=0; i--)
	cout << arr[i] << endl;	//or cout << *(p + i) << endl;
	
    return 0;
}

