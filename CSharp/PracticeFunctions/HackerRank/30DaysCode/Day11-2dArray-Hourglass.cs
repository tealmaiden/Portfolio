using System.CodeDom.Compiler;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Solution {

    static int hourglass(int[][] arr)
    {
        int longest = 0;
        for (int i=0; i<arr.Length-2; i++)
        {                       
            for (int j=0; j<arr[i].Length-2; j++)
            {
                int temp = 0; 
                temp += (arr[i][j]+arr[i][j+1]+arr[i][j+2]);
                //Console.Write(arr[i][j]+arr[i][j+1]+arr[i][j+2] + " ");
                temp += (arr[i+1][j+1]);
                //Console.Write(arr[i+1][j+1] + " ");
                temp += (arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]);
                //Console.Write(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]);
                //Console.WriteLine();
                if (i==0 && j==0)
                {
                    longest = temp;
                }
                else if (temp>longest)
                {
                    longest = temp;
                }
            }
        }
        return longest;
    }

    static void Main(string[] args) {
        int[][] arr = new int[6][];

        for (int i = 0; i < 6; i++) {
            arr[i] = Array.ConvertAll(Console.ReadLine().Split(' '), arrTemp => Convert.ToInt32(arrTemp));
        }
        
        Console.WriteLine(hourglass(arr));
           
    }
}
