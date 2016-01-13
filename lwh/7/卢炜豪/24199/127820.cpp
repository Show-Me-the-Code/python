#include<stdio.h>
int main()
{
    int n;
    while(1)
    {
        scanf("%d",&n);
        if(n==-1) break;
        int l=0;
        if(n==0) l=10;
        if(n>0&&n<=100)
        {
            l=10+n;
        }
        else if(n>100&&n<=1000)
        {
            l=110+2*(n-100);
        }
        else if(n>1000)
        {
            l=1910-(n-1000)*3;
        }
        printf("%d\n",l);
    }
}
