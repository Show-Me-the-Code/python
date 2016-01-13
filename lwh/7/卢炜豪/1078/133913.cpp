#include<stdio.h>
#include<math.h>
#define maxn 95
int isprime(int x);
int main()
{
    int x,y,a[maxn];
    while(scanf("%d %d",&x,&y)==2)
    {
        if(x==0&&y==0) break;
        int num=y-x+1;
        int z,count=0;

        for(int i=0;x<=y;i++)
        {
            a[i]=x*x+x+41;
            //a[i]=x;
            z=isprime(a[i]);
            //printf("z=%d\n",z);
            if(z==1) count++;
            x++;
        }
        //printf("count=%d num=%d\n",count,num);
        if(count==num)
            printf("OK\n");
        else if(count!=num)
            printf("Sorry\n");

    }

}
int isprime(int x)
{
    int n; int s;int i=0;
    s=sqrt(x);
    for(n=1;n<=s;n++)
    {
        if(x%n==0)
        i++;
    }

        if(i!=1)
        return 0;
        else
        return 1;
        i=0;
}
