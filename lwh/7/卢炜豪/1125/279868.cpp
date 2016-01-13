#include<stdio.h>
#define maxn 20+2

int lcm(int a[],int n);
int gcd(int a[],int ai,int n);
int main()
{
    int a[maxn],b[maxn];//数组a记录每排人数，数组b记录余下不够一排的人数
    int T;
    while(scanf("%d",&T)!=EOF)
    {
        for(int i=0;i<T;i++)
            scanf("%d %d",&a[i],&b[i]);//读入数据

        if(T==1)
        {
            printf("%d\n",a[0]+b[0]);
        }


        else
        {

        int sum=a[0],x0=a[0]+b[0];
        for(int k=0;;k++)
        {
            if((x0+k*a[0])%a[1]==b[1])
            {
                x0=x0+k*a[0];
             //   printf("1x0=%d\n",x0);
                 break;
            }

        }
        for(int i=1;i<T-1;i++)
        {

            int lcm2=lcm(a,i);//求最小公倍数
           // printf("lcm2=%d\n",lcm2);
            for(int k=0;;k++)
            if((x0+k*lcm2)%a[i+1]==b[i+1])
                {
                   x0=x0+k*lcm2;
                  // printf("x0=%d\n",x0);
                   break;
                }

        }

        printf("%d\n",x0);
        }
    }
}
int lcm(int a[],int n)
{
    int i=0,sum,lcm2=a[0];
    while(i!=n)
    {
        sum=1;
        for(int j=i;j<i+2;j++)
            sum=sum*a[j];


        lcm2=sum/gcd(a,lcm2,n);

        i++;

    }
    return lcm2;

}

int gcd(int a[],int ai,int n)
{
    if(a[n]<ai)
    {
        int temp=ai;
        ai=a[n];
        a[n]=temp;
    }
    while(a[n]%ai!=0)
    {
        int temp=ai;
        ai=a[n]%ai;
        a[n]=temp;

    }
    return ai;

}
