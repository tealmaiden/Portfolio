using System;
using System.Collections.Generic;

namespace NullableTypes
{
    class Program
    {
        static void Main()
        {
            //Default value for reference types is null:
            string name = null;

            //Default value for value types is 0:
            //int i = null; (can't do this for example)

            //To make value types nullable, use ?:
            int? i = null;

            bool? trueorfalse = null;
            if (trueorfalse == true)
            {
                Console.WriteLine("true");
            }
            else if (trueorfalse == false)
            {
                Console.WriteLine("false");
            }
            else
            {
                Console.WriteLine("null");
            }

            //null coalescing operator
            int? TicketsOnSale = 10;
            int AvailableTickets = TicketsOnSale ?? 0;

            Console.WriteLine(string.Format("avail tickets: {0}", AvailableTickets));

            /*What this is doing is removing need for if function:
            int AvaliableTickets = 0;

            if(TicketsOnSale == null)
            {
                AvaliableTickets = 0;
            }
            else
            {
                //no implicit conversion between nullable and nonnullable type
                //can do the following:
                AvaliableTickets = TicketsOnSale.Value; //add .value  
                AvaliableTickets = (int)TicketsOnSale; //call int
            }*/

            //https://www.youtube.com/watch?v=HuLJbiqpIM0
        }
    }
}

       

