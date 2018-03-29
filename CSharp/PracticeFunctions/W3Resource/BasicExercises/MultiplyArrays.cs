using System;
using System.Collections.Generic;

class MultiplyArrays
{
    public static int[] multiplyArrays(int[] arr1, int[] arr2)
    {
        int[] productArray = new int[4];
        for (int i = 0; i < productArray.Length; i++)
        {
            productArray[i] = arr1[i]*arr2[i];
        }
        return productArray;       

    }
    
    public static void Main()
    {
        int[] array1 = new int[] { 1, 3, -5, 4};
        int[] array2 = new int[] { 1, 4, -5, 2 };
        int[] prod = multiplyArrays(array1, array2);
        foreach (int num in prod)
        {
            Console.Write(num + " ");            
        }
        Console.WriteLine("\n");        
    }
}

