#include<stdio.h>
int main()
{
    int n;
    while(scanf("%d",&n)!=EOF)
    {
        int s;int a[n];int max=0,min=0;double sum=0;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&s);
            a[i]=s;
           // printf("a[%d]=%d",i,s);
        }
        max=a[0];
        for(int i=1;i<n;i++)
        {
           // max=a[0];
            if(a[i]>max) max=a[i];
           //else if(a[i]<a[i+1])max=a[i-1];
        }
     //   printf("max=%d\n",max);
       min=a[0];
       for(int i=1;i<n;i++)
       {

           if(a[i]<min) min=a[i];
       }
       //printf("min=%d\n",min);
      for(int i=0;i<n;i++)
       {
           sum=sum+a[i];
       }
       sum=sum-min-max;
       sum=sum/(n-2);
       printf("%.2lf\n",sum);

    }
}
