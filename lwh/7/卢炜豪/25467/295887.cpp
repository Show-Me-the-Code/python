#include <cstdio>
#include <cmath>
int main()
{
    int T;
    scanf("%d",&T);
    while(T)
    {
        int n,c[10000+5];
        c[0]=0;int max=-1;
        scanf("%d",&n);
        c[n+1]=0;
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&c[i]);
        }
         //   if(c[i]<0)
         //       c[i]=-c[i];
            for(int i=1;i<=n;i++)
            {
                int a=0,b=0;
                for(int j=0;j<i;j++)
                    a=a+c[j];
                  //  printf("a=%d ",a);
                for(int j=n;j>i;j--)
                    b=b+c[j];
                  //  printf("b=%d\n",b);
                  //  printf("%d\n",fabs(a-b));
                if(fabs(a-b)>max)
                    max=fabs(a-b);


            }

           printf("%d\n",max);

        T--;
    }
    return 0;
}
