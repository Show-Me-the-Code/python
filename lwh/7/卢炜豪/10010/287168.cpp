#include <stdio.h>
int step(int n);
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int stairs;
        scanf("%d",&stairs);
        printf("%d\n",step(stairs));
    }
    return 0;
}

int step(int n)
{
    int a[40+5];
    a[1]=1;a[2]=1;
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
