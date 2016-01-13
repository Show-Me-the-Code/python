#include<stdio.h>
#define P 1000
int main()
{
    int T,n,a[P];
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        scanf("%d",&n);
        int num=0;
        for(int j=0;j<n;j++)
        {
            for(int k=0;k<4;k++)
            {
                scanf("%d",&a[num]);
                num++;
            }

        }
        int count=0,q=0;
        for(int i=0;i<n;i++)
        {
          if(a[q]<60||a[q+1]<60||a[q+2]<60||a[q+3]<60)
                {
                count++;

                }
           q=q+4;
        }
        printf("%d\n",count);
    }


}
