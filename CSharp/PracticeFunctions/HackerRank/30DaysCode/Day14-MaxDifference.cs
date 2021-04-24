using System;
using System.Linq;

class Difference {
    private int[] elements;
    public int maximumDifference;

    // Add your code here
    public Difference(int[] e)
    {
        elements = e;
    }
    
    public int computeDifference()
    {
        for(int i=0; i < elements.Length; i++)
        {            
            for(int j=i+1; j < elements.Length; j++)
            {
                int temp = Math.Abs(elements[i]-elements[j]);
                if (temp>maximumDifference)
                {
                    maximumDifference=temp;
                }
            }
        }
        return maximumDifference;
    }
    
    
} // End of Difference Class

class Solution {
    static void Main(string[] args) {
        Convert.ToInt32(Console.ReadLine());
        
        int[] a = Console.ReadLine().Split(' ').Select(x=>Convert.ToInt32(x)).ToArray();
        
        Difference d = new Difference(a);
        
        d.computeDifference();
        
        Console.Write(d.maximumDifference);
    }
}
