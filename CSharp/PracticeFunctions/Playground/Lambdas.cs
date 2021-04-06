using System.Collections.Generic;
using System.Linq;
using System;

public static void Main(string[] args) 
{	
  //convert integer to array of ints
  int n = 49844;
  int[] result1 = n.ToString().Select(c=> Convert.ToInt32(c)).ToArray(); //wrong
  int[] result2 = n.ToString().Select(c => (int)Char.GetNumericValue(c)).ToArray();

  foreach(int n in result1)
  {
    Console.WriteLine(n); //returns ASCII codes, not desired
  }
  foreach(int n in result2)
  {
    Console.WriteLine(n); //correct
  }
  Console.WriteLine("length: " + result2.Length);


  //populate list with lambda
  List<int> chocolates = new List<int> {1,2,3,4};
  List<string> chocolateStrings = new List<string>();
  chocolateStrings = (List<string>)chocolates.Select(choc => choc.ToString()).ToList();
  Console.WriteLine(string.Join("woo", chocolateStrings));
}
