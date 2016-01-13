#include <cstdio>
#include <cstring>
int main()
{
	int n;
	char p[999999];

	scanf("%d",&n);
	getchar();
	while(n--)
	{
		int A[30],book;
		memset(A,0,sizeof(A));
		gets(p);
		int len = strlen(p);

		for(int i = 0 ;i < len;i++)
		{
			if((p[i] >= 97 && p[i] <= 122) || (p[i] >= 65 && p[i] <= 90))
			{
				if(p[i] >= 97 && p[i] <= 122)
				{
					A[p[i] - 96]++;
					//printf("%d\n",p[i]-64);
				}
				else if(p[i] >= 65 && p[i] <= 90)
				{
					A[p[i] - 64]++;
					//printf("%d\n",p[i]-64);
				}
			}
		}
		int min = 9999;
		for(int i = 1; i <= 26;i++)
		{
		    //printf("A[%d]=%d\n",i,A[i]);
			if(A[i] < min)
				min = A[i];
		}

		if(min == 1)
		{
			printf("Pangram!\n");
		}
		else if(min == 2)
		{
			printf("Double pangram!!\n");
		}
		else if(min == 3)
		{
			printf("Triple pangram!!!\n");
		}
		else if(min == 0)
		{
			printf("Not a pangram\n");
		}
	}

}
