using System;

public class SwapCharacters
{
    public static string swapChar(string str)
    {
        return str.Length > 2 ? 
            str.Substring(str.Length - 1) + 
            str.Substring(1, str.Length - 2) + 
            str.Substring(0, 1) 
            : str;
    }
    public static void Main()
    {
        Console.WriteLine(swapChar("undah the sea"));
    }
}
