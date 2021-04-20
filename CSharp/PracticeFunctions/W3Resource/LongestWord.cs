using System;
using System.Collections.Generic;

class LongestWord
{
    public static string findLongestWord(string sentence)
    {
        string[] senArray = sentence.Split(' ');
        string longWord=""; //need a default value 
        int compare=0;
        foreach (string word in senArray)
        {
           if (word.Length>compare)
            {
                compare = word.Length;
                longWord = word;
            }
        }
        return longWord;
    }
    public static void Main()
    {
        Console.WriteLine(findLongestWord("anda the sea"));
    }
}
