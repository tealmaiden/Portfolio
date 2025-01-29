using System;
using System.Runtime.InteropServices;

// 🔹 Define the Type Library GUID (Matches the Library GUID in IDL)
[assembly: Guid("D068F42B-A556-4188-8FF2-792AAF6D0B42")]

namespace SimpleComRegisteredLibrary
{
	[ComVisible(true)] // Makes the interface visible to COM
	[Guid("D9CA3BE3-610E-4251-82B7-11FEFAA45F33")] // Interface GUID (Matches IDL Interface GUID)
	public interface ISimpleComRegistered
	{
		string Test(); // A simple method that returns a "Hello" string
	}

	[ComVisible(true)] // Makes the class visible to COM
	[Guid("77676CBD-E536-4B98-9841-0AC794051191")] // Class GUID (Matches IDL CoClass GUID)
	[ClassInterface(ClassInterfaceType.None)] // Explicitly implements the interface
	public class SimpleComRegistered : ISimpleComRegistered
	{
		public SimpleComRegistered()
		{
			Console.WriteLine("SimpleComRegistered instantiated.");
		}

		public string Test()
		{
			Console.WriteLine("Test method called.");
			return "Hello from SimpleComRegistered!";
		}
	}
}
