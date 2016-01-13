#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
int main()
{
    int T;
    scanf("%d",&T);
    while(T)
    {
        int v;double b[10000+5];double a[10000+5];
        int m=0,n=0;
        scanf("%d",&v);

        for(int i=0;i<v;i++)
        {
            double k;
            scanf("%lf",&k);
            if(k>=0)
            {
                a[m]=k;
                m++;
            }
            else if(k<0)
            {
                b[n]=k;
                n++;
            }

        }
        sort(a,a+m);
        sort(b,b+n);
        double sum=0,sum1=0;
         if(v==1)
            sum1=sum=0;
        if(v==2)
        {


        if(m==1)
            sum=a[0];
        if(n==1)
            sum1=0;
        }


        for(int i=1;i<v;i++)
        {
            sum=sum+a[i];
        //    printf("%lf\n",sum);
            sum1=sum1+b[i];
        }


        printf("%.0lf\n",fabs(sum+sum1));

        T--;
    }
    return 0;
}
