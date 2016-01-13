#include<stdio.h>
int main()
{
    int n;int cow[56]={0,1,2,3,4};
    while(scanf("%d",&n)==1&&n!=0)
    {
       if(n>=4)
       {
           for(int i=4;i<56;i++)
           {
               cow[i]=cow[i-1]+cow[i-3];
           }
       }
       printf("%d\n",cow[n]);
    }
}
