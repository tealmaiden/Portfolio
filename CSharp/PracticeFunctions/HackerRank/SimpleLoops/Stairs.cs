using System;

namespace Test
{
    public class Stairs
    {
        internal static void Staircase(int n)
        {
            for (string i = ""; i.Length <= n; i = i + "#")
            {
                Console.WriteLine(i);
            }
        }
        
    }
}
