#include <stdio.h>
#define maxn 20+2

int gcd(int a[],int n);

int main()
{
    int T,a[maxn],b[maxn],x0,k,lcm;
    while(scanf("%d",&T)!=EOF)
    {
    int sum=1;
    for(int i=0;i<T;i++)
    {
    scanf("%d %d",&a[i],&b[i]);
    }
    if(T==1) printf("%d\n",a[0]+b[0]);
    else
    {
    x0=a[0]+b[0];
    sum=a[0];

    for(int i=0;i<T-1;i++)
    {
        for(int j=0;j<=i;j++)
        sum=sum*a[j];//求数组的乘积

       // printf("sum=%d gcd=%d ",sum,gcd(a,i));
        lcm=sum/gcd(a,i);
    //    printf("lcm=%d ",lcm);

        for(k=1;;)
        {
            if(((x0+k*lcm)%a[i+1])==b[i+1])
            {

                x0=x0+k*lcm;
        //        printf("i=%d k=%d x0=%d\n",i,k,x0);
                break;
            }
            k++;

        }
        sum=1;
    }
    int sum1=1;
    for(int i=0;i<T;i++)
        sum1=sum1*a[i];
    printf("%d\n",x0%sum1);
    }
    }
    }

int gcd(int a[],int n)
{
    int gcd1=a[0];
    if(n==0)
        return gcd1=a[0];
    else
    for(int i=1;i<=n;i++)
    {

    if(a[i+1]<a[i])
    {
    int temp=a[i+1];
    a[i+1]=a[i];
    a[i]=temp;
    }
    //交换了大小

    gcd1=a[i];
    int x=a[i+1];int y=gcd1;
    while(x%y!=0)
    {
    int temp=y;
    y=x%y;
    x=temp;
    }
    gcd1=y;
    }
    return gcd1;


}
