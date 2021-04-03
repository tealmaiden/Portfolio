using System;

namespace TryCatchFinally
{
    class TryFinallyTest
    {        
        static void ProcessString(string s)
        {
            if (s == "test")
            {
                throw new Exception(); // counts a "test" s as an exception 
            }
        }

        static void Main()
        {
            string s = "test"; // For demonstration purposes.

            try
            {
                ProcessString(s);
            }

            catch (Exception e)
            {
                Console.WriteLine("{0} Exception caught.", e);
            }

            finally
            {
                Console.WriteLine("finally");
            }
        }
    }
}
//https://msdn.microsoft.com/en-us/library/0yd65esw.aspx
