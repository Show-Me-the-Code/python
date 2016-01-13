#include<stdio.h>
#include<math.h>
int main()
{
    double n,m;
    while(scanf("%lf %lf",&n,&m)!=EOF)
    {
        double k=0,h;
        for(int i=0;i<m;i++)
        {

           // h=sqrt(n);
            k=n+k;
            n=sqrt(n);
        }
        printf("%.2lf\n",k);
    }
}
