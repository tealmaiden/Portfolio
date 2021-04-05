using System;
// you can also use other imports, for example:
// using System.Collections.Generic;

// you can write to stdout for debugging purposes, e.g.
// Console.WriteLine("this is a debug message");

class Solution {
	public int solution(int N) 
	{
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
			if (i!=Nints.Length-1 && Nints[i+1]==1)
			{
			    ends1=true;
			    if (temp>longest)
			    {
				longest= temp;
			    }
			    temp = 0;
			}       
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
		Console.WriteLine("longest: " + solution(49844));
	}
}
