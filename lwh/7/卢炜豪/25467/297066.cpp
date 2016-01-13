#include <cstdio>
#include <cmath>
int main()
{
    int T;
    scanf("%d",&T);
    while(T)
    {
        int n,a[10000+5],b[10000+5],c[10000+5];
        int sum=0,sum1=0;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%d",&a[i]);
        }
        a[0]=0;a[n+1]=0;
        for(int i=0;i<n;i++)
        {
            sum=sum+a[i];
            b[i]=sum;
          //  printf("b[%d]=%d\n",i,b[i]);
        }
        for(int i=n+1,q=0;i>=2;i--,q++)
        {
            sum1=sum1+a[i];
            c[q]=sum1;
          //  printf("c[%d]=%d\n",q,c[q]);
        }
        int max=0;
        for(int i=0;i<n;i++)
        {
            int k=b[i]-c[n-1-i];
            if(fabs(k)>max)
                max=fabs(k);
        }
        printf("%d\n",max);

        T--;
    }
}
