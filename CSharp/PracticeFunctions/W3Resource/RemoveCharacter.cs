using System;

public class RemoveCharacter
{
    public static string rmvChar(string str, int n)
    {
        return str.Remove(n, 1);
    }
    public static void Main ()
    {
        string a = "undah the sea";
        Console.WriteLine(rmvChar(a, 4));
        Console.WriteLine(rmvChar(a, 5));
        Console.WriteLine(rmvChar(a, 0));
    }
}
