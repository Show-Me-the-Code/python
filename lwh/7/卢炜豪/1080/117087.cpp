#include<stdio.h>
int main()
{
    int m,n;
    while(scanf("%d %d",&m,&n)!=EOF)
    {
        int a[m];int temp=2,i,sum=0;
        for(i=0;i<m;i++)
        {
            a[i]=temp;
            temp+=2;
        }
       // for(i=0;i<m;i++) printf("%d ",a[i]);
       if(m%n==0)
       {
           int k=0;
           for(int q=0;q<m/n;q++)
           {
           for(int t=0;t<n;t++)
           {
               sum=sum+a[k];
               k++;
           }
           k=k;
           if(q==0) printf("%d",sum/n);
           else if(q!=0)printf(" %d",sum/n);
           sum=0;
           }
           printf("\n");

       }
       else if(m%n!=0)
       {
           int w=m%n,sum1=0;
           for(int t=m-1;t>=m-w;t--)
           {
               sum1=sum1+a[t];
           }
            int k=0;
           for(int q=0;q<(m-w)/n;q++)
           {
           for(int t=0;t<n;t++)
           {
               sum=sum+a[k];
               k++;
           }
           k=k;
           printf("%d ",sum/n);
           sum=0;
           }
           printf("%d\n",sum1/w);



       }
    }
}
