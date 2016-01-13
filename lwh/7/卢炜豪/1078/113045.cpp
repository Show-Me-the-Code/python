#include<stdio.h>
#include<math.h>
int isprime(int sum);
int main()
{
    int n;int x,y;
    while(1)
    {
        if(x==0&&y==0) break; int sum;int index;
        scanf("%d %d",&x,&y);
        for(int i=x;i<=y;i++)
        {

            sum=pow(i,2)+i+41;
           // int l=sqrt(sum);
           // printf("%d\n",l);
            index=isprime(sum);

        } if(index==(sum-2)) printf("Yes\n");
    }
    return 0;
}
int isprime(int sum)
{
    int t=0;
    for(int d=2;d<sum;d++)
    {

        if(sum%d==0) printf("OK\n");
        if(sum%d!=0) t++;


    }
    return t;
}
