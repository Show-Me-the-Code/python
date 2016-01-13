#include<stdio.h>
int main()
{
    int m,n;
    while(1)
    {
      //  int sum=0;
        scanf("%d %d",&m,&n);
        if(m==-1&&n==-1) break;
        int num=n-m+1;int a[num];
        for(int i=0;m<=n;i++)
        {
            a[i]=m;
            m++;
          // printf("a[%d]=%d",i,a[i]);
        }
        for(int i=0;i<num;i++)
        {
            int sum=0;
            for(int k=1;k<a[i];k++)
            {
                int l;
                if(a[i]%k==0)
                {
                    l=k;
                    sum=sum+l;
                   // printf("l=%d ",l);
                }

            }
           if(sum==a[i]) printf("%d ",a[i]);
        }
printf("\n");
    }

    return 0;
}
