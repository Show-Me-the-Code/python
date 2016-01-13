#include <stdio.h>
#define maxn 20+2

int gcd(int a[],int n);

int main()
{
    int T,a[maxn],sumbook,b[maxn],t,q,x0,min,k,k1,lcm;
    while(scanf("%d",&T)!=EOF)
    {
        q=0;
    int sum=1;
    for(int i=0;i<T;i++)
    {
    scanf("%d %d",&a[i],&b[i]);
    }
    if(T==1) printf("%d\n",a[0]+b[0]);


    else
    {
    x0=a[0]+b[0];
    sum=a[0]*a[1];
    lcm=a[0];
  //  printf("1.sum=%d gcd=%d x0=%d\n",sum,gcd(a,0),x0);
    for(int i=1;i<T;i++)
    {

        for(k=1,k1=1;;)
        {

            if(i<=1)
            {

            if(((x0+k*a[i-1])%a[i])==b[i])
            {
               // printf("x0=%d ",x0);
                x0=x0+k*a[i-1];
             //   printf("2.i=%d k=%d x0=%d\n",i,k,x0);
                k=1;
                break;
            }
            k++;
            }
            else
            {

            for(int j=i;j<i;j++)
                sum=sum*a[j];
            lcm=sum/gcd(a,i);
          //  printf("2.5sum=%d lcm=%d gcd=%d\n",sum,lcm,gcd(a,i));
            if(((x0+k1*lcm)%a[i])==b[i])
            {
                x0=x0+k1*lcm;
                if(i==2)
                    t=x0;
              //  printf("3.q=%d sum=%d lcm=%d i=%d k1=%d x0=%d\n",q,sum,lcm,i,k1,x0);
                break;
            }
            k1++;
            sum=a[0]*a[1];
            }
        }
    }



    }
    printf("%d\n",t);
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
    //½»»»ÁË´óÐ¡

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

