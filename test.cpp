#include<iostream>
using namespace std;

int main()
{
	int n = 4;
	int a[n][n], b[n][n], c[n][n];
	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < n; ++j)
		{
			if(i==j)
			{
				a[i][i] = 1;
				b[i][i] = 1;	
			}
			else
			{
				a[i][j] = 0;
				b[i][j] = 0;
			}
		}		
	}

	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < n; ++j)
		{
			c[i][j] = 0;
			for(int k = 0; k < n; ++k)
			{
				c[i][j] += a[i][k] * b[k][j]; 
			}
		}
	}

	for(int i = 0; i < n; ++i)
	{
		for(int j = 0; j < n; ++j) 
		{
			cout<<c[i][j]<<" ";
		}
		cout<<endl;
	}

		return 0;
}
