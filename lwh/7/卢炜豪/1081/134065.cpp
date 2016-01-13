#include<stdio.h>
int main()
{
    int a[100],i,n,min,minpos;
    while(scanf("%d",&n)!=EOF)
    {
        if(n==0)
            break;
        else
            for(i=0;i<n;i++)
            scanf("%d",&a[i]);
            min=a[0];
            minpos=0;
            for(i=0;i<n;i++)
            {
                if(a[i]<min)
                {
                    min=a[i];
                    minpos=i;   //增加找到最小元素所在的下标
                }

            }
                a[minpos]=a[0];
                a[0]=min;

                for(i=0;i<n;i++)
                {
                    printf("%d ",a[i]);
                }
                printf("\n");

    }
            return 0;
}
