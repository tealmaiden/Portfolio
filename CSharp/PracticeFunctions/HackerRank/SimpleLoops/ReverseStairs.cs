using System;
using System.Linq;

public class ReverseStairs
{
    internal static void RevStaircase(int n)
    {
        if (1 <= n && n <= 100)
        {
            for (string i = ""; i.Length <= n; i = i + "#")
            {
                string spaces = string.Concat(Enumerable.Repeat(" ", n - i.Length)); //Enumerable.Repeat repeats number of indicated characters (spaces) up to the specified length
                Console.WriteLine(spaces + i);
            }
        }
        else
        {
            Console.WriteLine("\n  Retry and enter a number between 1 and 100.");
        }
    }    
}
