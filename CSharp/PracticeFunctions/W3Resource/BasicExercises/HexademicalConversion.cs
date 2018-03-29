using System;
using System.Collections.Generic;

class HexademicalConversion
{
    public static void Main()
    {
        Console.WriteLine("enter a hexademimal");

        int dec = int.Parse(Console.ReadLine(), System.Globalization.NumberStyles.HexNumber);

        Console.WriteLine(dec);

        string hex = dec.ToString("X");

        Console.WriteLine(hex);
    }
}

