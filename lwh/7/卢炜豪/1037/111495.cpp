#include<stdio.h>
double cal(int n);
int main()
{
    int x,n;
    scanf("%d",&x);
    for(int i=1;i<=x;i++)
    {
        scanf("%d",&n);
       cal(n);
    }
}
double cal(int n)
{
    double t=1,j=1,i;double sum=0;
    for(i=1;i<=n;i++)
    {
        sum=sum+(double)(j*(1/t));
        t=t+1;
        j=-j;

    }
   printf("%.8lf\n",sum);
}
