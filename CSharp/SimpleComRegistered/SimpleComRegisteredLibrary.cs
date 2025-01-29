using System;
using System.IO;
using System.Runtime.InteropServices;
using Microsoft.Win32;

// 🔹 Define the Type Library GUID (Matches the Library GUID in IDL)
[assembly: Guid("D068F42B-A556-4188-8FF2-792AAF6D0B42")]

namespace SimpleComRegisteredLibrary
{
	[ComVisible(true)]
	[Guid("D9CA3BE3-610E-4251-82B7-11FEFAA45F33")] // Interface GUID (Matches IDL Interface GUID)
	public interface ISimpleComRegistered
	{
		string Test();
	}

	[ComVisible(true)]
	[Guid("77676CBD-E536-4B98-9841-0AC794051191")] // Class GUID (Matches IDL CoClass GUID)
	[ClassInterface(ClassInterfaceType.None)]
	public class SimpleComRegistered : ISimpleComRegistered
	{
		public SimpleComRegistered()
		{
			File.AppendAllText("C:\\Temp\\SimpleComRegisteredLog.txt", "SimpleComRegistered instantiated.\n");
		}

		public string Test()
		{
			File.AppendAllText("C:\\Temp\\SimpleComRegisteredLog.txt", "Test method called.\n");
			return "Hello from SimpleComRegistered!";
		}

		// 🔹 Register Function (Writes CLSID to Windows Registry)
		[ComRegisterFunction]
		public static void RegisterFunction(Type t)
		{
			try
			{
				string clsid = t.GUID.ToString("B");
				using (RegistryKey key = Registry.ClassesRoot.CreateSubKey(@"CLSID\" + clsid))
				{
					key.SetValue("", "SimpleComRegistered Class");
					key.CreateSubKey("InprocServer32").SetValue("", "mscoree.dll"); // Uses .NET runtime
					key.CreateSubKey("ProgID").SetValue("", "SimpleComRegisteredLibrary.SimpleComRegistered");
				}

				File.AppendAllText("C:\\Temp\\SimpleComRegisteredLog.txt", "COM Registered Successfully.\n");
			}
			catch (Exception ex)
			{
				File.AppendAllText("C:\\Temp\\SimpleComRegisteredLog.txt", "COM Registration Failed: " + ex.Message + "\n");
			}
		}

		// 🔹 Unregister Function (Removes CLSID from Registry)
		[ComUnregisterFunction]
		public static void UnregisterFunction(Type t)
		{
			try
			{
				string clsid = t.GUID.ToString("B");
				Registry.ClassesRoot.DeleteSubKeyTree(@"CLSID\" + clsid, false);

				File.AppendAllText("C:\\Temp\\SimpleComRegisteredLog.txt", "COM Unregistered Successfully.\n");
			}
			catch (Exception ex)
			{
				File.AppendAllText("C:\\Temp\\SimpleComRegisteredLog.txt", "COM Unregistration Failed: " + ex.Message + "\n");
			}
		}
	}
}