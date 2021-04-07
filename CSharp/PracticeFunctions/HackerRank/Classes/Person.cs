using System;
using System.Collections.Generic;
using System.IO;

class Person 
{
    public int age;    
    
    //Getters and Setters:
    protected int getAge()
    {
        return this.age;
    }
    
    protected void setAge(int newAge)
    {
        this.age = newAge;             
    }
    
    //Constructor that initializes age:
    public Person(int initialAge) 
    {
        if(initialAge>0)
        {
            setAge(initialAge);
        }
        else
        {
            setAge(0);
            Console.WriteLine("Age is not valid, setting age to 0.");
        }
     }
     
     public void amIOld() 
     {
         int currentAge = getAge();
         if (currentAge<13)
         {
             Console.WriteLine("You are young.");
         }
         else if (currentAge>=13 && currentAge <18)
         {
             Console.WriteLine("You are a teenager.");
         }
         else
         {
             Console.WriteLine("You are old.");
         }
     }
     
     //Increment age:
     public void yearPasses() 
     {
        setAge(getAge()+1);
     }
     
     static void Main(String[] args) {
        int T=int.Parse(Console.In.ReadLine());
        for (int i = 0; i < T; i++) {
            int age=int.Parse(Console.In.ReadLine());
            Person p=new Person(age);
             p.amIOld();
                for (int j = 0; j < 3; j++) {
                  p.yearPasses();
                }
                p.amIOld();
                Console.WriteLine();
        }
    }
}
