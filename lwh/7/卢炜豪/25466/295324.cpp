#include <cstdio>
long long int num[35][35];
int main()
{
     for(int i=0;i<33;i++)
    {
        num[i][0]=0;
    }
    num[1][1]=1;num[2][1]=1;num[2][2]=1;num[0][0]=0;num[3][1]=1;num[3][2]=2;num[3][3]=1;num[0][1]=1;
    int q=33;
    for(int i=1;i<32;i++)
        for(int j=1;j<=i;j++)
    {
        num[i][j]=num[i-1][j-1]+num[i-1][j];
    }
     num[1][1]=1;num[2][1]=1;num[2][2]=1;num[0][0]=0;num[3][1]=1;num[3][2]=2;num[3][3]=1;
    int T;
    scanf("%d",&T);
    for(int t=0;t<T;t++)
    {
        int n;
        scanf("%d",&n);
        n=n+1;
        if(n==1)
            printf("1\n");
        else if(n==2)
            printf("1 1\n");
        else
        {
            for(int i=1,l=i,r=i;i<=n;i++,l++,r++)
            {
               if(i!=n)
                printf("%lld ",num[n][i]);
                else
                    printf("%lld\n",num[n][i]);
            }

        }
    }
}
