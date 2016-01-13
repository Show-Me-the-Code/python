/*

*/
#include <cstdio>
#include <cstring>
int cow[1000005];
int main()
{
	int N,K,t,ans = -1,temp = -1;
	memset(cow,0,sizeof(cow[0]));
	scanf("%d %d",&N,&K);
	for(int i= 0;i < N;i++)
	{
		scanf("%d",&t);
		if(cow[t]!=0)
		{
			if(i - cow[t] <= K)
				temp = t;
            if(ans < temp)
			ans = temp;
		}

		cow[t] = i;
	}
	printf("%d\n",ans);
}
