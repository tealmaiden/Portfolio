#include "stdafx.h"
using namespace std;
using namespace System;
using namespace System::Collections;

//Challenge
//https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/

	static String^ adjust(String^ longer, String^ shorter)
	{
		String^ adjKey = "";
		while (adjKey->Length <= longer->Length)
		{
			adjKey = adjKey + shorter;
		}
		return adjKey = adjKey->Substring(0, longer->Length);
	}
	static String^ encrypt(String^ message, String^ key)
	{
		String^ alphabet = "abcdefghijklmnopqrstuvwxyz";
		String^ encryption = "";
		key = adjust(message, key);

		for (int i = 0; i<message->Length; i++)
		{
			int alpha = alphabet->IndexOf(message[i]);
			int beta = alphabet->IndexOf(key[i]);
			Char^ letter;
			if (alpha + beta<26)
			{
				letter = alphabet[alpha + beta];
			}
			else
			{
				letter = alphabet[beta - 26 + alpha];
			}
			encryption = encryption + letter;
		}
		return encryption;
	}
	int main()
	{
		Console::WriteLine("enter a message");
		String^ message = Console::ReadLine();
		Console::WriteLine("enter a key, shorter than the message");
		String^ key = Console::ReadLine();
		Console::WriteLine(encrypt(message, key));
		return 0;
	}
