using System;

public class Ex4_WriteArray
{
    public static float[] array_of_calcs()
    {
        float a = -1 + 4 * 6;
        float b = (35 + 5) % 7;
        float c = 14 + -4 * 6 / 11;
        float d = 2 + 15 / 6 * 1 - 7 % 2;

        return new float[] { a, b, c, d };
    }



    public static void Main()
    {
        foreach (float i in array_of_calcs())
        {
            System.Console.WriteLine(i.ToString());
        }
    }
}
