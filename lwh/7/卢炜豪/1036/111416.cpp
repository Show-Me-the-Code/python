#include<stdio.h>
int weisu(int x);
int yusan(int x);
int main()
{
    int x;
    while(scanf("%d",&x)!=EOF)
    {
        weisu(x);
        yusan(x);
    }
}
int weisu(int x)
{
    int i,j;
    for(i=0;x>=1||x<=-1;i++)
    {
        j=x%10;
        x=x/10;
    }
    printf("%d ",i);

    return i;
}
int yusan(int x)
{
    int k,i;

    k=x%3;

    printf("%d\n",k);
}
