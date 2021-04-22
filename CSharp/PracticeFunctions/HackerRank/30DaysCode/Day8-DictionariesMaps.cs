using System;
using System.Collections.Generic;
using System.IO;
class Solution 
{
    static void Main(String[] args) {
        int n = Convert.ToInt32(Console.ReadLine());        
        Dictionary<string, string> contactdictionary = new Dictionary<string, string>();
        for (int i = 0; i < n; i++)
        {
            string[] contacts = Console.ReadLine().Split(' ');
            if (contacts[0]!=null && contacts[1]!=null)
            {
                contactdictionary.Add(contacts[0], contacts[1]);
            }           
        }
        //int ntries=10^5;
        while (true)
        {
            try
            {
                string input = Console.ReadLine();
                if (contactdictionary.ContainsKey(input))
                {
                    Console.WriteLine(input+'='+contactdictionary[input]);
                }
                else
                {
                    Console.WriteLine("Not found");
                }                
            }
            catch(Exception e)
            {
                break;
            }
            
            //ntries-=1;
            
        }
    }
}
