using System;

public class BooleansConditionals
{
    public static bool checkNegative(int a, int b)
    {
        return a * b < 0 ? true : false;
        //if(a*b<0) { return true; }
        //else { return false; }
    }
    public static void Main()
    {
        Console.WriteLine(checkNegative(1,-2));
        Console.WriteLine(checkNegative(0, -2));
        Console.WriteLine(checkNegative(1, 1));

        Console.WriteLine("\nInput first integer:");
        int x = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Input second integer:");
        int y = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Check if one is negative and one is positive:");
        Console.WriteLine((x < 0 && y > 0) || (x > 0 && y < 0));
        Console.WriteLine(x * y < 0);
    }
}
