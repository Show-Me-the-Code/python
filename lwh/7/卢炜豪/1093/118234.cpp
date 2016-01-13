#include<stdio.h>
int main()
{
    int n;
    while(1)
    {
        scanf("%d",&n);
        if(n==0) break;
        int a[n];
        for(int i=0;i<n;i++)
        scanf("%d",&a[i]);

        int i,j;
        for(i=0;i<n-1;i++)
        {
            for(j=0;j<n-1;j++)
            {
                if(a[j]<a[j+1])
                {
                    int temp;
                    temp=a[j+1];
                    a[j+1]=a[j];
                    a[j]=temp;
                }
            }
        }
        for(int t=0;t<n;t++)
        {
            if(t==n-1) printf("%d",a[t]);
                else printf("%d ",a[t]);
        }
        printf("\n");
    }
}
