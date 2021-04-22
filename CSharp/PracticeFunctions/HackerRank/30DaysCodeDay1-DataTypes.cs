using System;
using System.Collections.Generic;
using System.IO;

class Solution {
    static void Main(String[] args) {
        int i = 4;
        double d = 4.0;
        string s = "HackerRank ";
        
        // Declare second integer, double, and String variables.
        int i2 = 0;
        double d2 = 0;
        string s2;
           
        // Read and save an integer, double, and String to your variables.    
        s2 = Console.In.ReadLine();
        i2 = Convert.ToInt32(s2);
        i+=i2;
       
        //Console.WriteLine("enter an double");
        s2 = Console.ReadLine();
        d2 = Convert.ToDouble(s2);
        d+=d2;
        
        //Console.WriteLine("enter an string");
        s2 = Console.ReadLine();
        s+=s2;
        
        // Print the sum of both integer variables on a new line.
        Console.WriteLine(i);
        
        // Print the sum of the double variables on a new line.
        Console.WriteLine("{0:0.0}",d);
        
        // Concatenate and print the String variables on a new line
        Console.WriteLine(s);
        // The 's' variable above should be printed first.

    }
}
