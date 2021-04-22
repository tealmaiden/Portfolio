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

class Solution 
{
    public static void printNotWeird()
    {
        Console.WriteLine("Not Weird");
    }

    public static void printWeird()
    {
        Console.WriteLine("Weird");
    }
    
    public static void weird(int n)
    {
        if(n<1 || n>100)
        {
            return;
        }
        if(n%2!=0)
        {
            printWeird();
        }
        else if(n%2==0)
        {
            if (n>=2 && n<=5)
            {
                printNotWeird();
            }
            else if (n>6 && n<=20)
            {
                printWeird();
            }
            else if (n>20)
            {
                printNotWeird();
            }    
        }
    }


    public static void Main(string[] args) 
    {
        int N = Convert.ToInt32(Console.ReadLine());
        weird(N);
    }
}
