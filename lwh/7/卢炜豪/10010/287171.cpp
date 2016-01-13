#include <stdio.h>
long long int step(int n);
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int stairs;
        scanf("%d",&stairs);
        printf("%lld\n",step(stairs));
    }
    return 0;
}

long long int step(int n)
{
    long long int a[40+5];
    a[0]=1;a[1]=1;
    if(n<=2)
    {
        return a[n];
    }
    else
    {

    for(int i=2;i<n;i++)
    {
        a[i]=a[i-1]+a[i-2];
    }

    return a[n-1];
    }
}
