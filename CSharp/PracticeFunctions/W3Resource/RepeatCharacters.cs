using System;

public class RepeatCharacters
{
    public static string repChar(string str)
    {
        return str.Length > 1 ?
            str.Substring(0, 1) +
            str +
            str.Substring(0, 1)
            : str;
    }
    public static void Main()
    {
        Console.WriteLine(repChar("undah the sea"));
    }
}
