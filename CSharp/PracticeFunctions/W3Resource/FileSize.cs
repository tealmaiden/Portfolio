using System;
using System.Collections.Generic;
using System.IO;

class FileSize
{
    public static void Main()
    {
        string path = "C:\\Users\\h8048069\\Documents\\SVNProjects\\W3Exercises\\W3Exercises\\FileSizeTest.txt";
        
        long length = new System.IO.FileInfo(path).Length;
        Console.WriteLine(length);

        FileInfo file = new FileInfo(path);
        long length2 = file.Length;
        Console.WriteLine(length2);
    }

}

