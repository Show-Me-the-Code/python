#include<stdio.h>
int main()
{
    int x,m,a,b,c,d,e,f,i,j,k;
    while(scanf("%d",&x)!=EOF&&x!=0)
    {
        k=0;
        for(i=0;i<x;i++)
        {
            scanf("%d",&m);
            a=m/100;
            b=m%100/50;
            c=m%100%50/10;
            d=m%100%50%10/5;
            e=m%100%50%10%5/2;
            f=m%100%50%10%5%2;
            k=k+a+b+c+d+e+f;
        }
        printf("%d\n",k);
    }
}
