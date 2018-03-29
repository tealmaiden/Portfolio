using System;
//other versions possibly need System.Collections.Generic for Math to work

class AbsValue
{
    public static bool checkClose(int n)
    {
        return (Math.Abs(100 - n) <= 20) || (Math.Abs(200 - n) <= 20);
        //? true : false;
    }

    public static void Main()
    {
        Console.WriteLine("enter a number");
        int val = int.Parse(Console.ReadLine());
        Console.WriteLine(checkClose(val));
    }
}
