#include <cstdio>
#include <cmath>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        if(n==0)
            break;
        double a[10000+10];
        for(int i=0;i<n;i++)
            scanf("%lf",&a[i]);
        double mid=a[n-1]-(fabs(a[n-1]-a[0]))/2;
     //   printf("%lf\n",a[n-1]-(fabs(a[n-1]-a[0]))/2);
    //    printf("mid=%lf\n",mid);
        double last=0;
        for(int i=0;i<n;i++)
        {
            last=last+fabs(a[i]-mid);
        }
        printf("%.0lf\n",last);

    }
}
