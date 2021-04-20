using System;

public class DigitRectangle
{

    public static void Main()
    {
        Console.WriteLine("Enter a digit: ");
        int digit = int.Parse(Console.ReadLine());
        Console.WriteLine("{0}{0}{0}", digit);
        Console.WriteLine("{0} {0}", digit);
        Console.WriteLine("{0} {0}", digit);
        Console.WriteLine("{0} {0}", digit);
        Console.WriteLine("{0}{0}{0}", digit);
    }
}
