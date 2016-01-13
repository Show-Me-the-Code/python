#include<stdio.h>
int main()
{
    int m,n,minmax;
    while(1)
    {
        scanf("%d %d",&m,&n);
        if(m==-1&&n==-1) break;
        int a,b;
        a=m;b=n;
        int temp;
        temp=m%n;

        for(;temp!=0;)
        {
            m=n;
            n=temp;
            temp=m%n;
        }
        minmax=a*b/n;

        printf("%d %d\n",n,minmax);
    }
}
