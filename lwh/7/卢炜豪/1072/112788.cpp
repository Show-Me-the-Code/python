#include<stdio.h>
int main()
{
    int m,n,a;
    while(1)
    {
        int data0=0,data1=0;
        scanf("%d %d %d",&n,&m,&a);
        if(m==0&&n==0&&a==0) break;
        data0=2*(m+a);
        data1=data0-n;

        printf("%d\n",data1);
    }
}
