#include <cstdio>

int N,A[20],dif[20][20],value[20];

struct Cow
{
	char re;
	int a,b;
}cow[20];

int find(int x)
{
	return A[x] == x ? x : find(A[x]);
}

void merge(int a,int b)
{
	int t1 = find(a);
	int t2 = find(b);

	if(t1 != t2)
		A[t2] = t1;
}

int DFS(int n)
{
	int kont = find(n);
	if(value[kont])
		return DFS(n+1);
	if(n > N)
		return 1;
    bool Y_or_N[4] = {true,true,true,true};
	for(int i = 1;i <= N;i++)
	{
		if(dif[kont][i] == 1 && value[i] != 0)
		{
			Y_or_N[value[i]] = false;
		}
	}
	int ans = 0;
	for(int i = 1;i <= 3;i++)
	{
		if(Y_or_N[i])
		{
			value[kont] = i;
			ans += DFS(n+1);
			value[kont] = 0;
		}
	}

	return ans;
}
int main()
{
	int K;
	scanf("%d %d",&N,&K);
	//getchar();
    for(int i = 1;i <= N;i++)
		A[i] = i;
	for(int i = 1;i <= K;i++)
    {
        scanf(" %c %d%d",&cow[i].re,&cow[i].a,&cow[i].b);
        //getchar();
    }
    //for(int i = 1;i <= K;i++)
    //    printf("%c %d %d\n",cow[i].re,cow[i].a,cow[i].b);
	for(int i = 1;i <= K;i++)
	{
		if(cow[i].re == 'S')
			merge(cow[i].a,cow[i].b);
	}
	for(int i = 1;i <= K;i++)
    {
        if(cow[i].re == 'D')
        {
            dif[find(cow[i].a)][find(cow[i].b)]=1;
            dif[find(cow[i].b)][find(cow[i].a)]=1;
        }
    }
	//int ab=0;
   // for(int i = 1;i <= N;i++)
   // if(A[i]==i)
    //ab++;
    //printf("ab=%d\n",ab);
	printf("%d\n",DFS(find(1)));
}
