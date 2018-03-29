using System;

public class RepeatNumber
{

    public static void Main()
    {
        Console.WriteLine("Enter a number: ");
        int number = int.Parse(Console.ReadLine());
        Console.WriteLine("{0} {0} {0} {0}", number);
        Console.WriteLine("{0}{0}{0}{0}", number);
        Console.Write(number);
        Console.Write(" ");
        Console.Write(number);
        Console.Write(" ");
        Console.Write(number);
        Console.Write(" ");
        Console.Write(number);
        Console.WriteLine();
        Console.Write(number);
        Console.Write(number);
        Console.Write(number);
        Console.Write(number);
        Console.WriteLine();
    }
}
