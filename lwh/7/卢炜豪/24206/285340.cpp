#include <stdio.h>

#define maxn 100000000+2

double f[maxn];
double fi(int n);
int main()
{
    int n;
    f[1]=1;f[2]=7;
    while(scanf("%d",&n)!=EOF)
    {
        double w;

        if(n==0)
            break;

        if(n==1)
            w=1;
       else if(n==2)
            w=7;
        else if(n>=3)
        {
            w=fi(n);
        }
        printf("%.0lf\n",w);
    }
}

double fi(int n)
{
    if(n==2||n==1)
    {
        if(n==2)
           f[n]=7;
        if(n==1)
            f[n]=1;
    }
    else
    {
        f[n]=(int)(3*n*n-3*n+1)%2013;
      //  printf("%.0lf\n",f[n]);
        f[n]=(int)(f[n]+fi(n-2))%2013;
    }

    return f[n];
}
