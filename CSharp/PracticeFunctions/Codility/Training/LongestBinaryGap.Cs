using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

					
public class Program
{
	//Complete the solve function below
	public static int solution(int N) {
	 //write your code in C# 6.0 with .NET 4.5 (Mono)

	int longest = 0;
	int temp = 0;
	bool ends1 = false;
	string Nstring = Convert.ToString(N, 2);
	//Console.WriteLine(Nstring);

	int [] Nints = new int[Nstring.Length];

	for(int i=0; i<Nstring.Length; i++)
	{
	    Nints[i] = int.Parse(Nstring[i].ToString());
	}

	for(int i = 0; i<Nints.Length; i++)
	{
	    if(temp==0 && i!=0 && Nints[i]==0 && Nints[i-1]==1)
	    {
	      temp+=1;
	      ends1=false;             
	    }
	    else if(temp!=0 && Nints[i]==0 && i!=((Nints.Length)-1) && Nints[i+1]==0)
	    {
		temp+=1;				
	    }
	    else if (Nints[i]==0 && i!=((Nints.Length)-1) && Nints[i+1]==1)
	    {
		temp += 1;
		if(temp>longest)
		{
		    longest = temp;            
		}
		temp=0;
		ends1=true;
		Console.WriteLine("reset: " + i);
	    }
	    else if (i==(Nints.Length)-1 && Nints[i]==0)
	    {
	      if(temp>longest && ends1==true)
	      {
		  longest = temp;
	      }
	    }
        }
        return longest;
    }

    public static void Main(string[] args) 
    {
       Console.WriteLine("longest: " + solution(1376796946));			
    }
}
