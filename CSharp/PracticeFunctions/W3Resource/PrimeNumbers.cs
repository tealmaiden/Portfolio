using System;
using System.Collections.Generic;

public class PrimeNumbers
{
    /// <summary>
    /// tests if prime
    /// </summary>
    /// <param name="n"></param>
    /// <returns></returns>    
    public static bool IsPrime(int n)
    {
        if (n==0||n==1)
        { return false; }

        for (int i=2; i<n; i++)
        {
            if (n%i==0)
            {
                return false;
            }            
        }
        return true;
    }
    /// <summary>
    /// sums a list of integers
    /// </summary>
    /// <param name="list"></param>
    /// <returns></returns>
    public static int sumList(List<int> list)
    {
        int sum = 0;
        foreach (int prime in list)
        {
            sum = sum + prime;
        }
        return sum;
    }
    /// <summary>
    /// creates list of prime numbers sequentially until the specified amount of primes is reached
    /// </summary>
    /// <param name="amtPrimes"></param>
    /// <returns></returns>
    public static List<int> listAmtPrimes(int amtPrimes)
    {
        List<int> primeList = new List<int>();
        int i = 0;
        while (primeList.Count < amtPrimes)
        {
            if (IsPrime(i))
            {
                primeList.Add(i);
            }
            i++;
        }
        return primeList;
    }
    /// <summary>
    /// sums the amount of prime numbers indicated, starting from the first prime.
    /// </summary>
    /// <param name="amtPrimes"></param>
    /// <returns></returns>
    public static int sumAmountFirstPrimes(int amtPrimes)
    {
        return sumList(listAmtPrimes(amtPrimes));
    }

    ///// <summary>
    ///// filters every prime number within a number into a list
    ///// </summary>
    ///// <param name="containerNum"></param>
    ///// <returns></returns>
    //public static List<int> filterPrime(int containerNum)
    //{
    //    List<int> primeList = new List<int>();
    //    for (int i=0; i<containerNum; i++)
    //    {
    //        if (IsPrime(i))
    //        {
    //            primeList.Add(i);
    //        }
    //    }
    //    return primeList;
    //}

    ///// <summary>
    ///// returns the sum of all prime numbers contained in a number
    ///// </summary>
    ///// <param name="d"></param>
    ///// <returns></returns>
    //public static int sumPrimesContainedIn(int d)
    //{
    //    return sumList(filterPrime(d));
    //}
    public static void Main()
    {
        List<int> test = listAmtPrimes(500);
        foreach (int n in test)
        {
            Console.WriteLine(n);
        }
        Console.WriteLine(sumAmountFirstPrimes(500));
        //Console.WriteLine(sumPrimesContainedIn(500));
    }
}
