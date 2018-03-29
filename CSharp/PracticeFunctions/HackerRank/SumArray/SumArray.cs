using System;


namespace Test
{
    class SumArray
    {
        static void sum(int[] numbers) //numbers is the array, the input entries that come after the first input
        {            
            int summ = 0;
            foreach (int k in numbers)
            {
                summ = summ + k;
            }
            Console.WriteLine(summ); 
        }

        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    int n = Convert.ToInt32(Console.In.ReadLine()); //convert console input to 32 bit integer

                    while (1 <= n && n <= 10000) //constraint on size of n. the program just quits if out of range.
                    {
                        int[] vals = new int[n]; //creates array of size n from input
                        
                        for (int i = 0; i < n; i++) //checks if vals[i] is non-integer
                        {
                            string read = Console.In.ReadLine();
                            try
                            {
                                vals[i] = Convert.ToInt32(read);
                            }

                            catch (System.FormatException e)
                            {
                                Console.WriteLine("Exception caught: {0}", e);
                                Console.WriteLine("\n Enter a number");
                                continue;
                            }

                            if (1 <= vals[i] && vals[i] <= 10000) //constraint on size of input value
                            {
                                vals[i] = vals[i];
                            }

                            else
                            {
                                Console.WriteLine("Enter number between 1 and 10,000");
                                continue;
                            }

                        }
                        sum(vals);
                        break;
                    }

                    break;
                }

                catch (System.FormatException e) //catch if n is non-integer
                {
                    Console.WriteLine("Exception caught: {0}", e);
                    Console.WriteLine("\n Enter a number");                    
                }

            }          
            

        }
    }
}
