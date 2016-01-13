#include<stdio.h>
#define maxn 50005
int main()
{
    int T;
    scanf("%d",&T);
    for(int TT=0;TT<T;TT++)
    {
        int n,a[maxn],count=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        scanf("%d",&a[i]);

        for( int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(a[i]>a[j])
                    count++;
            }
        }
        printf("%d\n",count);
    }
}
