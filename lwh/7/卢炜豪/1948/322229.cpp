#include <cstdio>
#include <cstring>

const int M = 500;
const int N = 500;
int Max_(int n,int *A)
{
	 int sum = -999999999,temp = -999999999;
	// for(int i = 0;i <= n;i++) printf("A[%d]=%d\n",i,A[i]);
     //printf("\n");
	 for(int i = 0;i <= n;i++)
	 {
		 if(temp > 0)
			temp += A[i];
		else
			temp = A[i];

		 if(temp > sum)
			 sum = temp;
	 }
	 return sum;
}
int main()
{
	int m,n;
	//int Martix[M][N],col[N],ans = -999999999 ;//col[N] store the volue of each coloum number;

	while(scanf("%d %d",&m,&n) !=EOF)
	{

	//int m,n;
	int Martix[M][N],col[N],ans = -999999999 ;
	for(int i = 0;i < m;i++)
	{
		for(int j = 0;j < n;j++)
		{
			scanf("%d",&Martix[i][j]);
		}
	}

	//memset(col,0,sizeof(col[0]));

	for(int i = 0;i < m;i++)  //遍历的起点行
	{
	    for(int w = 0;w < n;w++)
            col[w] = 0;

		for(int j = i;j < m;j++)
		{
			for(int k = 0;k < n;k++)
			{
				col[k] += Martix[j][k];
				int max_ = Max_(k,col);
				//printf("max=%d col[%d]=%d\ni=%d j=%d k=%d\n\n",max_,k,col[k],i,j,k);
				if(max_ > ans)
					ans = max_;
                //printf("ans=%d\n",ans);
			}
		}
	}

	printf("%d\n",ans);
	}
	return 0;
}
