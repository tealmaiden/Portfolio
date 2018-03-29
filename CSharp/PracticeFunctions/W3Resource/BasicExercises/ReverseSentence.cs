using System;
using System.Collections.Generic;

class ReverseSentence
{
    public static string reverSen(string sentence)
    {
        string[] senArray = sentence.Split(' ');
        string reversed = "";
        for (int i = senArray.Length-1; i>=0; i--)
        {
            reversed = reversed + senArray[i] + " ";
        }
        return reversed;
    }
    public static void Main()
    {
        Console.WriteLine(reverSen("what's a fire and why does it, what's the word, buuuurn"));
    }
}

