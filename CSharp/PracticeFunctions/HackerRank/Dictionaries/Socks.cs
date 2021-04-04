public class Program
{
	public static int sockMerchant(int[] ar) {
        Dictionary<int, int> socks = new Dictionary<int, int>();
        foreach(int color in ar)
        {
            if (socks.ContainsKey(color))
            {
                socks[color]+=1;
            }
            else{
                socks[color]=1;
            }
        }
        
        Dictionary<int, int> pairs = new Dictionary<int, int>();
        foreach(KeyValuePair<int, int> color in socks)
        {
            int key  = color.Key;
            int numColors = socks[color.Key];
            int numPairs = (int)numColors/2;
            pairs.Add(key, numPairs);
        }
        
        int sumPairs = 0;
        foreach(KeyValuePair<int, int> pair in pairs)
        {
            sumPairs+=pair.Value;
        }
        
        return sumPairs;
    }

	public static void Main()
	{
		int [] ar = {1,2,3,1,2,3,1,1,3,3};
		Console.WriteLine(sockMerchant(ar));
	}
}
