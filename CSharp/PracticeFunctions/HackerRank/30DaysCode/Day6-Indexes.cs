using System;
using System.Collections.Generic;
using System.IO;
using System.Text;

class Solution 
{
    static void evensOddStrings(List<string> strings)
    {
        foreach (string item in strings)
        {
            string newString = "";
            StringBuilder sb = new StringBuilder(item);
            for (int i = 0; i< sb.Length; i=i+2)
            {
                newString += sb[i].ToString();
            }
            newString+=" ";
            for (int j = 1; j<sb.Length; j=j+2)
            {
                newString += sb[j].ToString();
            }
            Console.WriteLine(newString);
        }
        
    }
    static void Main(String[] args) {
        
        int n = Convert.ToInt32(Console.ReadLine());
        List<string> strings = new List<string>();
        for (int i=0; i<n; i++)
        {
            string item = Console.ReadLine();
            strings.Add(item);            
        }
        evensOddStrings(strings);                       
        
    }
}
