using System;
using System.Collections.Generic;

class NumberSwap
    {
        public static void Main()
        {
            int num_a, num_b, temp;

            Console.WriteLine("Input the First Number : ");
            num_a = int.Parse(Console.ReadLine());
            
            Console.WriteLine("Input the Second Number : ");
            num_b = int.Parse(Console.ReadLine());
                 
            temp = num_a;
            num_a = num_b;
            num_b = temp;

            Console.WriteLine("after swapping : ");

            Console.WriteLine("first number : " + num_a);
            Console.WriteLine("second number : " + num_b);
        }
    }

