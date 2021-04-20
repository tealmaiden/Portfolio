using System;
using System.Collections.Generic;

class SumDigits
{
    public static int sumDigits(int n)
    {        
        int sum = 0;
        while(n>=1)
        {
            sum = sum + (n % 10);
            n = n / 10;
        }
        return sum;
    }
    public static void Main()
    {
        Console.WriteLine("enter an integer");
        int entry = int.Parse(Console.ReadLine());
        Console.WriteLine(sumDigits(entry));
    }
}

