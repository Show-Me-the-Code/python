#include<stdio.h>
#include<math.h>
int main()
{
    int m,n;
    while(scanf("%d %d",&m,&n)!=EOF)
    {

    int i,sum0=0,sum1=0;

    int l=n-m+1;int a[l*l];
    for(i=0;i<l,m<=n;i++)
    {
        a[i]=m;
        m++;
    }

    for(i=0;i<l;i++)
    {
        if(a[i]%2==0)
            sum0=sum0+pow(a[i],2);
        else  if(a[i]%2!=0)
                sum1=sum1+pow(a[i],3);

    }
   printf("%d %d\n",sum0,sum1);
    }
    return 0;
}
