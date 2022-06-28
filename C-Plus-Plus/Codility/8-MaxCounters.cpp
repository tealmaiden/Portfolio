#include <iostream>
#include <vector>
using namespace std;

vector<int> solution(int N, vector<int>& A) 
{  
    vector<int> counter = vector<int>(N, 0);
    int nup = N + 1;
    int MC = 0;
    int counterValue = 0;

    for (int k = 0; k < A.size(); k++)
    {
        int X = A[k];

        if (X == nup)
        {
           counter = vector<int> (N, MC);
        }

        else
        {
            counter[X - 1] += 1;
            counterValue = counter[X - 1];
            if (counterValue > MC)
            {
                MC = counterValue;
            }            
        }
    }

    return counter;
}

void main()
{
    vector<int> A = { 3, 4, 4, 6, 1, 4, 4 };
    vector<int> Ans = solution(5, A);
    cout << "\n";
    for (int i = 0; i < size(Ans); i++)
    {
        cout << Ans[i];
    }

}
