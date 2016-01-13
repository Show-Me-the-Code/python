#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
const int Max=100005;
/*struct PKpai
{
	int num;
	int loc;
}PK[Max];*/
/*int cmp(const void *a,const void *b)
{
	return return *(PKpai *a).num > *(PKpai *b).num ? 1 : -1;
}*/
int main()
{
	int N,ans=0,max_=0;
	int B[Max],C[Max],PK[Max];
	memset(B,0,sizeof(B[0]));
	scanf("%d",&N);
	for(int i = 1;i <= N;i++)
	{
		scanf("%d",&PK[i]);
		//B[PK[i].num]++;
		//if(max_<PK[i]);
		//max_=PK[i];

	}
	//qsort(PK+1,PK+N+1,cmp);
	PK[0]=PK[N+1]=0;
	//PK[N+1]=PK[N];
	for(int i=0;i<=N;i++)
	{
		ans+=fabs(PK[i]-PK[i+1]);
	}
	//ans/=2;
	printf("%d\n",ans/2);
}
