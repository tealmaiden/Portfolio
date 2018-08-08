# Alphabet Cipher

___
## Objective
Create a program that that functions as a vignere cipher, which uses the alphabet an a key word to encode a message. The key word and message are input values. Challenge link:
https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/

## Steps Taken
### Encryption
Drew out on paper how the encoding mechanism worked to better understand how it could be translated into code.

I determined that one way to look at the result is to see it as the index in the alphabet that is the of a the indices of each expanded key character and message character in a loop across the alphabet.

Being new to C++, I drafted what I would do in a familiar .NET language, C#, and converted using MSDN as a resource. This is why the sytax in my program relies on the System::String library rather than std::string standard C++ library. 

To use the key word, it needed to be repeated across the length of the message, so I made a function that repeated the key word until it was the same length as the message. 

Made loops that added the alphabet indices of key and message characters if the sum was less than 26 and some subtraction math if the sum was the same or greater.

Created console input functions to collect user key and message. Console displays the result.


## Results
The program works as expected. 
It won't work if key is longer than message, but that can be easily changed.
The ext step would be a decryption algorithm, which I had forgotten about until now.
