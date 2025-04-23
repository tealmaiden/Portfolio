//SimpleComRegisteredLibrary.cs

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
    [ClassInterface(ClassInterfaceType.None)] // Explicitly implements the interface
    public class SimpleComRegistered : ISimpleComRegistered
    {
        public SimpleComRegistered()
        {
            Log("✅ SimpleComRegistered instantiated.");
        }

        public string Test()
        {
            Log("✅ Test method called.");
            return "Hello from SimpleComRegistered!";
        }

        // 🔹 COM Registration Function (Stores CLSID & ProgID in Windows Registry)
        [ComRegisterFunction]
        public static void RegisterFunction(Type t)
        {
            try
            {
                // ✅ Ensure we're using .NET 9
                string runtimeVersion = System.Runtime.InteropServices.RuntimeEnvironment.GetSystemVersion();
                if (!runtimeVersion.StartsWith("9."))
                {
                    Log($"❌ ERROR: Incorrect .NET version detected: {runtimeVersion}. Expected .NET 9.");
                    return;
                }

                string clsid = t.GUID.ToString("B"); // Format as {GUID}
                string progID = t.Namespace + "." + t.Name; // "SimpleComRegisteredLibrary.SimpleComRegistered"
                string comHostPath = t.Assembly.Location.Replace(".dll", ".comhost.dll"); // Get full path to COM Host DLL

                Log($"🟡 Registering COM Object: {progID}");
                Log($"🟡 CLSID: {clsid}");
                Log($"🟡 COM Host Path: {comHostPath}");

                // ✅ Register CLSID
                using (RegistryKey clsidKey = Registry.ClassesRoot.CreateSubKey(@"CLSID\" + clsid))
                {
                    clsidKey.SetValue("", progID + " Class");

                    // ✅ InprocServer32 - Point to COMHOST.DLL instead of mscoree.dll
                    using (RegistryKey inprocKey = clsidKey.CreateSubKey("InprocServer32"))
                    {
                        inprocKey.SetValue("", comHostPath); // Load .NET 9 COM Host
                        inprocKey.SetValue("ThreadingModel", "Both");
                        inprocKey.SetValue("Assembly", t.Assembly.FullName);
                        inprocKey.SetValue("CodeBase", comHostPath);
                    }

                    // ✅ Register ProgID (for CreateObject)
                    using (RegistryKey progIDKey = clsidKey.CreateSubKey("ProgID"))
                    {
                        progIDKey.SetValue("", progID);
                    }
                }

                // ✅ Register ProgID for VBA / CreateObject
                using (RegistryKey progKey = Registry.ClassesRoot.CreateSubKey(progID))
                {
                    progKey.SetValue("", progID + " Class");
                    progKey.CreateSubKey("CLSID").SetValue("", clsid);
                }

                Log("✅ COM Registered Successfully under .NET 9.");
            }
            catch (Exception ex)
            {
                Log($"❌ COM Registration Failed: {ex.GetType()} - {ex.Message}\n{ex.StackTrace}");
            }
        }

        // 🔹 COM Unregistration Function (Removes CLSID & ProgID from Windows Registry)
        [ComUnregisterFunction]
        public static void UnregisterFunction(Type t)
        {
            try
            {
                string clsid = t.GUID.ToString("B");
                string progID = t.Namespace + "." + t.Name;

                Log($"🟡 Unregistering CLSID: {clsid}");
                Log($"🟡 Unregistering ProgID: {progID}");

                using (RegistryKey key = Registry.ClassesRoot.OpenSubKey(@"CLSID", writable: true))
                {
                    if (key?.OpenSubKey(clsid) != null)
                    {
                        key.DeleteSubKeyTree(clsid, false);
                        Log("✅ CLSID removed.");
                    }
                }

                using (RegistryKey key = Registry.ClassesRoot.OpenSubKey(progID, writable: true))
                {
                    if (key?.OpenSubKey(progID) != null)
                    {
                        key.DeleteSubKeyTree(progID, false);
                        Log("✅ ProgID removed.");
                    }
                }

                Log("✅ COM Unregistered Successfully.");
            }
            catch (Exception ex)
            {
                Log($"❌ COM Unregistration Failed: {ex.GetType()} - {ex.Message}\n{ex.StackTrace}");
            }
        }

        // 🔹 Logging Helper Function
        private static void Log(string message)
        {
            string logFile = "C:\\Temp\\SimpleComRegisteredLog.txt";
            File.AppendAllText(logFile, $"{DateTime.Now}: {message}\n");
            Console.WriteLine(message); // Also print to console
        }
    }
}
