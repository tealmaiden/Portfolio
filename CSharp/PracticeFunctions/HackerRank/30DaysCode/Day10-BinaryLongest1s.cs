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
    
    static int solution(int n)
    {
        string bin = Convert.ToString(n, 2);
        int binlen = bin.Length;
        int[] bints = new int[binlen];
        int temp = 0;
        int longest =0;
        
        for (int i=0; i<binlen; i++)
        {
            int num = Convert.ToInt32(bin[i].ToString());
            bints[i]=num;
        }
        
        for (int i=0; i<binlen; i++)
        {            
            if (i==0 && bints[i]==1)
            {                
                temp=1;
                if (bints[i+1]==0)
                {
                    if (temp>longest)
                    {
                        longest=temp; 
                    }
                    temp = 0;
                }               
            }
            
            else if(i!=0 && i!=(binlen-1) && bints[i]==1)
            {
                temp+=1;
                if (bints[i+1]==0)
                {
                    if (temp>longest)
                    {
                        longest=temp; 
                    }
                    temp = 0;
                }
            }
            
            else if(i==(binlen-1) && bints[i]==1)
            {
                temp+=1;
                if (temp>longest)
                {
                    longest=temp; 
                }
                temp = 0;
            }
        }
        
        return longest;
        
    }


    static void Main(string[] args) {
        int n = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine(solution(n));
        
    }
}
