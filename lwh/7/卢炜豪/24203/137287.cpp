#include<stdio.h>
int main()
{
    long long int k;int n;
    while(scanf("%lld %d",&k,&n)!=EOF)
    {
        int a[11],b[11];int w,count;
        if(k==0&&n==0) break;
        if(k%10==0)
        {
        for(int i=0;k>0;i++)
       {
          a[i]=k%10;
          b[i]=a[i];
          k=k/10;
          count=i;
      }
        for(int i=count;i>=0;i--) printf("%d",a[i]);
        printf("\n");
      }
      else
      {


      for(int i=0;k>0;i++)
      {
          a[i]=k%10;
          b[i]=a[i];
          k=k/10;
          count=i;
      }
      int s=count;
      int temp;
      for(int i=0;i<count;i++)
    {
      for(int j=1;j<=count;j++)
    {
      if(a[j]<a[j-1])
    {
      temp=a[j];
      a[j]=a[j-1];
      a[j-1]=temp;
    }
    }
    }
   // for(int i=s;i>=0;i--) printf("b[%d]=%d ",i,b[i]);
   // printf("\n");
   // for(int i=0;i<=count;i++) printf("a[%d]=%d ",i,a[i]);
   // printf("\n");

   int q=0,l;
  // printf("s=%d\n");
    for(int i=s;i>=0;i--)
    {
       // printf("q=%d ",q);
        for(int j=0;j<n;j++)
        {
            if(b[i]!=a[j]){ q=q+1;}
//printf("n=%d q=%d\n",n,q);
        }

        if(q==n) printf("%d",b[i]);

         q=0;
    }
    printf("\n");
      }


    }
}
