#include <cstdio>
#define Max 10000 + 10

int main()
{
	int n;int A[Max];int sum,temp_sum;
	while(scanf("%d",&n) != EOF)
	{
		//int A[Max];

		for(int i = 0;i < n;i++)
			scanf("%d",&A[i]);

		 sum = 0,temp_sum = 0;

		for(int i = 0;i < n;i++)
		{
			if(temp_sum > 0)
				temp_sum += A[i];
			else
				temp_sum = A[i];

			if(temp_sum > sum)
				sum = temp_sum;
		}

		printf("%d\n",sum);
	}
}
