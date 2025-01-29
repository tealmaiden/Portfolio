using System;
using System.Runtime.InteropServices;

// 🔹 Define the Type Library GUID (Matches the Library GUID in IDL)
[assembly: Guid("12345678-ABCD-1234-ABCD-1234567890AB")]

namespace SimpleComLibrary
{
	[ComVisible(true)] // Makes the interface visible to COM
	[Guid("87654321-DCBA-4321-DCBA-0987654321BA")] // Interface GUID (Matches IDL Interface GUID)
	public interface ISimpleCom
	{
		string Test(); // A simple method that returns a "Hello" string
	}

	[ComVisible(true)] // Makes the class visible to COM
	[Guid("98765432-CBA1-4321-CBA1-1234567890AB")] // Class GUID (Matches IDL CoClass GUID)
	[ClassInterface(ClassInterfaceType.None)] // Explicitly implements the interface
	public class SimpleCom : ISimpleCom
	{
		public SimpleCom()
		{
			Console.WriteLine("SimpleCom instantiated.");
		}

		public string Test()
		{
			Console.WriteLine("Test method called.");
			return "Hello from SimpleCom!";
		}
	}
}


