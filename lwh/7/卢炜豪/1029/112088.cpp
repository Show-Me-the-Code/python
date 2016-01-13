#include<stdio.h>
int main()
{
    int n;
    while(1)
    {
      scanf("%d",&n);
      if(n==0) break;
      int x;int a[n];int sum1=0,sum2=0;
      for(int i=0;i<n;i++)
      {
          scanf("%d",&x);
          a[i]=x;
      }

    for(int i=0;i<n;i++)
    {
        if(a[i]%2==0)
            sum1=sum1+a[i];
    }
    for(int i=0;i<n;i++)
    {
        if(a[i]%2!=0)
            sum2=sum2+a[i];
    }
    printf("%d %d\n",sum2,sum1);
    for(int i=n-1;i>=0;i--)
    {
        if(i!=0)
        printf("%d ",a[i]);
        else if(i==0) printf("%d",a[i]);
    }
    printf("\n");
}
return 0;
}
