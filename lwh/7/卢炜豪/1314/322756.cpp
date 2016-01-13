#include <cstdio>
#include <cstring>
const int Max = 100000+5;
int A[Max];
void init(int n)
{
	for(int i=0;i < n;i++)
		A[i]=i;
}
int GetF(int x)
{
    if (x != A[x])
    {
        A[x] = GetF(A[x]);     //回溯时的压缩路径
    }         //从x结点搜索到祖先结点所经过的结点都指向该祖先结点
    return A[x];
}

void merge(int a,int b)
{
	int a1,b1;
	a1=GetF(a);
	b1=GetF(b);
	if(a1 != b1)
	{
		A[b1]=a1;
	}
}
int main()
{
	int n;
	while(scanf("%d",&n)!=EOF)
	{
		int m,t;
		//int A[Max];
		init(n);//初始化数组
		scanf("%d",&m);
		for(int i=0;i < m;i++)
		{
			int a,b;
			scanf("%d %d",&a,&b);
			merge(a,b);
		}
		scanf("%d",&t);
		for(int i=0;i < t;i++)
		{
			int a,b;
			scanf("%d %d",&a,&b);
			int F1 = GetF(a);
			int F2 = GetF(b);
			if(F1 == F2)
				printf("y\n");
			else
				printf("n\n");
		}
	}
}
