using System;
using System.Collections.Generic;

namespace Enumerables
{
    //enums are stongly types constants. not implicitly interchangeable.
    //if a program uses a set of integers, enums may help make the program more readable and maintainable

    class Program
    {
        static void Main()
        {
            customer[] customers = new customer[3];

            //Instead of using numbers to distinguish male/female, can just use Gender.Male/Female, so it is harder to mix up:
            customers[0] = new customer
            {
                name = "mark",
                Gender = Gender.Male
            };

            customers[1] = new customer
            {
                name = "mary",
                Gender = Gender.Female
            };

            customers[2] = new customer
            {
                name = "sam",
                Gender = Gender.Unknown
            };

            foreach (customer customer in customers)
            {
                Console.WriteLine("name = {0} && Gender = {1}", customer.name, getGender(customer.Gender));
            }
        }

        //Type int changes to gender:
        public static string getGender(Gender gender)
        {
            switch (gender)
            {
                //Removing need for numbers here:
                case Gender.Unknown:
                    return "unknown";
                case Gender.Male:
                    return "male";
                case Gender.Female:
                    return "female";
                default:
                    return "invalid data";
            }
        }
    }

    //enums are value types.
    //numbers are implicitly assigned in enums. 
    //the default underlying type is int, but you can change it.
    //you can even assign any number to the enum values.
    public enum Gender
    {
        Unknown,
        Male,
        Female
    }

    // 0 - unknown
    // 1 - male
    // 2 - female

    public class customer
    {
        public string name { get; set; }
        //Type int changes to gender:
        public Gender Gender { get; set; }
    }

    /***Example Without Enums:'
    // It is hard to tell what the numbers refer to.
    class Program
    {
        static void Main()
        {
            customer[] customers = new customer[3];

            customers[0] = new customer
            {
                name = "mark",
                Gender = 1
            };

            customers[1] = new customer
            {
                name = "mary",
                Gender = 2
            };

            customers[2] = new customer
            {
                name = "sam",
                Gender = 0
            };

            foreach (customer customer in customers)
            {
                Console.WriteLine("name = {0} && Gender = {1}", customer.name , getGender(customer.Gender));
            }
        }

        public static string getGender(int gender)
        {
            switch (gender)
            {
                case 0:
                    return "unknown";
                case 1:
                    return "male";
                case 2:
                    return "female";
                default:
                    return "invalid data";
            }
        }      
    }
    
    // 0 - unknown
    // 1 - male
    // 2 - female

    public class customer
    {
        public string name { get; set; }
        public int Gender { get; set;  }
    }*/
}
//https://www.youtube.com/watch?v=HsTVTCP-c4w
