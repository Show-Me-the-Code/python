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
    int k, j, r;
    r = x;
    while(r != A[r])     //查找跟节点
        r = A[r];      //找到跟节点，用r记录下
    k = x;
    while(k != r)             //非递归路径压缩操作
    {
        j = A[k];         //用j暂存parent[k]的父节点
        A[k] = r;        //parent[x]指向跟节点
        k = j;                    //k移到父节点
    }
    return r;         //返回根节点的值
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
