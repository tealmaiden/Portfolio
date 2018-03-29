// GlassModelCalculator.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std; //not best practice to declare namespace, but it's easier if you don't need other namespaces. otherwise would need to put "std::" in front of objects below

//function to create dummy former results
void writeFormerOutput()
{
	string formerFileName;
	cout << "\nenter the former output file name: ";
	getline(cin, formerFileName);

	enum formerType { f0, f1, f2, f3, f4 };
	int formerAmounts[] = { 10, 11, 12, 13, 14 };

	ofstream outputFile(formerFileName);

	if (outputFile.is_open())
	{
		outputFile << "Former,Amount\n";

		for (int i = 0; i < 5; i++)
		{
			if (i == formerType::f0)
			{
				string Index;
				ostringstream convert;
				convert << formerAmounts[i];
				Index = convert.str();
				outputFile << "f0," +  Index + '\n';
			}
			else if (i == formerType::f1)
			{
				string Index;
				ostringstream convert;
				convert << formerAmounts[i];
				Index = convert.str();
				outputFile << "f1," + Index + '\n';
			}
			else if (i == formerType::f2)
			{
				string Index;
				ostringstream convert;
				convert << formerAmounts[i];
				Index = convert.str();
				outputFile << "f2," + Index + '\n';
			}
			else if (i == formerType::f3)
			{
				string Index;
				ostringstream convert;
				convert << formerAmounts[i];
				Index = convert.str();
				outputFile << "f3," + Index + '\n';
			}
			else if (i == formerType::f4)
			{
				string Index;
				ostringstream convert;
				convert << formerAmounts[i];
				Index = convert.str();
				outputFile << "f4," + Index + '\n';
			}
			else
			{
				cout << "Former type name mistmatch.";
			}
		}
		outputFile.close();
	}
	else
	{
		cout << "Unable to open file";
	}
	cout << "\nGlass former array data exported to " + formerFileName + '\n';
}

//function to read file content into array
void read(string nameIn, int nameArray[])
{
	string line;
	ifstream inputFile(nameIn); //open file - using ifstream to read for input, since you will be writing from a data structure rather than the file itself. fstream if reading for input and output

	stringstream lineStream(line);
	string cell;
	
	enum wasteType {a,b,c,d,e,f,g,h,i};
	
	int wtIndex = 0;
	
	if (inputFile.is_open())
	{		
		getline(inputFile, line); //skips first row
			
		for (int i = 0; i < 9; i++)
		{
			getline(inputFile, cell, ',');
			getline(inputFile, line);
			
			if (cell == "a")
			{
				int wtIndex = wasteType::a;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else if (cell == "b")
			{
				int wtIndex = wasteType::b;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else if (cell == "c")
			{
				int wtIndex = wasteType::c;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else if (cell == "d")
			{
				int wtIndex = wasteType::d;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else if (cell == "e")
			{
				int wtIndex = wasteType::e;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else if (cell == "f")
			{
				int wtIndex = wasteType::f;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else if (cell == "g")
			{
				int wtIndex = wasteType::g;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else if (cell == "h")
			{
				int wtIndex = wasteType::h;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else if (cell == "i")
			{
				int wtIndex = wasteType::i;
				int intLine;
				istringstream convert(line);
				if (!(convert >> intLine))
					cout << "No valid value for " + cell;
				nameArray[wtIndex] = intLine;
			}
			else
			{
				cout << "Please enter correct waste type names.";
			}
		}
		inputFile.close();
	}
	else cout << "Unable to open file";

	writeFormerOutput();
}

//test function to print array to console
void print(int nameArray[])
{
	cout << "\nWaste file data inputted to array: \n";
	for (int i = 0; i < 9; i++)
	{		
		cout << nameArray[i];
		cout << '\n';
	}
}

int main()
{
	//get names of the files; creates output file if not there
	string inFileName;
	string outFileName;
	cout << "enter the input file name: ";
	getline(cin, inFileName);
	
	//create array for waste amounts
	int wasteAmounts[10];

	//read file content and insert waste amounts into array
	read(inFileName, wasteAmounts);

	//test print input array to console
	print(wasteAmounts);

	return 0;
}