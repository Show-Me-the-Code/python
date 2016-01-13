#include <stdio.h>

int f(int n);
int main()
{
    int n;
//    f[1]=1;f[2]=7;
    while(scanf("%d",&n)!=EOF)
    {
        int w;

        if(n==0)
            break;

        if(n==1)
            w=1;
       else if(n==2)
            w=7;
        else if(n>=3)
        {
            w=f(n);
        }
        printf("%d\n",w);
    }
}

int f(int n)
{
    int sum;
    if(n%2!=0)
    {
            sum=((((n+1)/2%2013)*((n+1)/2%2013))%2013*((2*n-1)%2013))%2013;
    }
    else if(n%2==0)
    {
        sum=(((n/2%2013)*(n/2%2013))%2013*((2*n+3)%2013))%2013;
    }
    return sum;
}
