#include <cstdio>
int A[20],book[20];
void init(int N)
{
	for(int i = 1;i <= N;i++)
		A[i] = i;
}
int Find(int x)
{
	return A[x] == x ? x : Find(A[x]);
}
void merge(int a,int b)
{
	int t1 = Find(a);
	int t2 = Find(b);
	if(t1 != t2)
		A[t2] = t1;
}
int main()
{
	int N,K,breed = 0,breed1 = 0,breed2 = 0;
	char re;
	scanf("%d %d",&N,&K);
	getchar();

	init(N);

	for(int i = 0;i < K;i++)
	{
		int a,b;
		//scanf("%c",)
		scanf("%c %d %d",&re,&a,&b);
		getchar();
		if(re == 'S')
		{
			book[a]++;
			book[b]++;
			merge(a,b);
		}
	}

	for(int i = 1;i <= N;i++)
	{
		if(A[i] == i)
			breed++;
		if(book[i] == 0)
			breed2++;
	} //breed = breed1 + breed2;
	//printf("breed1=%d breed2=%d\n",breed1,breed2);
	int k = breed,ans = 0;
	//while(k != 0)
   // {
   //     ans += breed * k;
    //    k--;
  //  }
    printf("%d\n",6*breed);
}
