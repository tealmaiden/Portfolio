String formatting: string.Format("{0:" + formatString + "}", value) <br>
Console number formatting: Console.WriteLine("{0:0.0}", value); // writes a numerical value to one decimal place <br>
StringBuilder: Remove character at an index in a string
```
  string somestring = "abcdefg";
  StringBuilder sb = new StringBuilder(somestring);
  sb[3] = 'X'; // index starts at 0!
  somestring = sb.ToString();
  Console.WriteLine(sb); //https://www.arclab.com/en/kb/csharp/replace-or-remove-char-in-string-by-index.html
```
