using System;

public class Multiply
{
    public static void Main()
    {
        Console.WriteLine("Input the first number to multiply: ");
        int a = int.Parse(Console.ReadLine());
        Console.WriteLine("Input the second number to multiply: ");
        int b = int.Parse(Console.ReadLine());
        Console.WriteLine("Input the third number to multiply:");
        int c = int.Parse(Console.ReadLine());
        int d = a * b * c;
        Console.WriteLine("Output: {0} x {1} x {2} = {3}", a, b, c, d);
    }
}
